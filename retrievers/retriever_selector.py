from langchain_core.prompts import load_prompt

from llm import TechPriestLLM
import os
from retrievers.selector_prompt import selector_prompt
from retrievers.rules_prompt import rules_prompt
from rules import rules_dir


class RetrieverSelector:
    def __init__(self):
        self.llm = TechPriestLLM()

    @staticmethod
    def load_rule_prompt(intention):
        intention_to_file = {
            "core_concepts": "0_core_concepts.md",
            "battle_round": "0_battle_round.md",
            "command": "1_command.md",
            "movement": "2_movement.md",
            "shooting": "3_shooting.md",
            "charge": "4_charge.md",
            "fight": "5_fight.md",
            "weapons_abilities": "0_weapons_habilities.md",
            "data_sheet": "0_data_sheets.md",
            "deployment_abilities": "0_deployment_abilities.md",
        }
        file_name = intention_to_file.get(intention)
        if file_name is None:
            raise Exception("No intention found")

        print(f"rules_dir={rules_dir}\tfile_name={file_name}")

        try:
            with open(os.path.join(rules_dir, file_name), "r") as doc_rules:
                rules = doc_rules.read()

            return rules_prompt + rules

        except FileNotFoundError:
            raise FileNotFoundError(f"File `{file_name}` not found")

    def call(self, user_query, conversation):
        print(f"IN SELECTOR:\nUSER QUERY: {user_query}\nCONVERSATION: {conversation}")
        response = self.llm.get_intention(prompt=selector_prompt, user_query=user_query)
        intention = response["retriever"]  # TODO falta guardarail para intenciones no listadas
        match intention:
            case "emperor_cheering":
                yield "Por el Emperador!"
            case "tech_priest":
                yield "Rezando al Omnissiah"
            case _:
                prompt = self.load_rule_prompt(intention)
                for chunk in self.llm.prey_conversation(prompt=prompt, user_query=user_query):
                    yield chunk
