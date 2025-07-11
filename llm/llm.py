from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.runnables import RunnablePassthrough
from langfuse.langchain import CallbackHandler
from settings import settings
from langfuse import Langfuse

langfuse = Langfuse(
    secret_key=settings.langfuse_secret_key,
    public_key=settings.langfuse_public_key,
    host=settings.langfuse_host,
)
langfuse_handler = CallbackHandler()


class TechPriestLLM:
    def __init__(self):
        self.llm = ChatOpenAI(
            api_key=settings.llm_api_key,  # LM Studio normalmente no requiere key o acepta cualquier string
            base_url=settings.llm_url,
            model=settings.llm_model,
            streaming=True
        )
        self.memory = ConversationBufferMemory(return_messages=True)

    def get_llm(self):
        return self.llm

    def save_to_memory(self, user_query, response):
        self.memory.chat_memory.add_user_message(user_query)
        self.memory.chat_memory.add_ai_message(response)

    def reset_memory(self):
        self.memory.clear()

    def prey(self, prompt, user_query):
        chat = ChatPromptTemplate.from_messages([
            ("system", prompt),
            ("human", "{user_query}")
        ])

        chain = chat | self.llm | JsonOutputParser()

        return chain.invoke({"user_query": user_query}, config={"callbacks": [langfuse_handler]})

    def get_intention(self, prompt, user_query):
        chat = ChatPromptTemplate.from_messages([
            ("system", prompt),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{user_query}")
        ])

        chain = (RunnablePassthrough.assign(
            history=lambda _: self.memory.load_memory_variables({})[
                "history"]) | chat | self.llm | JsonOutputParser())

        response = chain.invoke({"user_query": user_query}, config={"callbacks": [langfuse_handler]})

        print(f"RESPONSE: {response}")

        return response

    def prey_conversation(self, prompt, user_query):
        chat = ChatPromptTemplate.from_messages([
            ("system", prompt),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{user_query}")
        ])

        chain = (RunnablePassthrough.assign(
            history=lambda _: self.memory.load_memory_variables({})[
                "history"]) | chat | self.llm | StrOutputParser())

        response_chunks = chain.stream({"user_query": user_query}, config={"callbacks": [langfuse_handler]})

        full_response = ""
        for chunk in response_chunks:
            print(chunk, end="", flush=True)
            full_response += chunk
            yield full_response  # → streaming hacia Gradio

        self.save_to_memory(user_query, full_response)
