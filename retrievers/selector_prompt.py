selector_prompt = """
Teniendo en cuenta la conversación con el usuario, tu deber es detectar que información requiere el usuario para
poder desarrollar su partida de warhammer 40K.

Detecta el la intención sobre la petición o necesidad del usuario.

Los intenciones o información posibles son:
    * `core_concepts` : conceptos clave sobre como jugar
    * `battle_round` : orden y desarrollo de la partida
    * `command` : fase de comando
    * `movement`: fase de movimiento
    * `shooting` : fase de disparo
    * `charge` : fase de carga
    * `fight` : fase de lucha
    * `weapons_abilities` : listado de habilidades de las armas
    * `data_sheet` : información sobre como se estructuran las hojas de datos
    * `deployment_abilities` : listado de las habilidades de despliege de las unidades
    * `emperor_cheering` : para cualquier alabanza al dios emperador
    * `tech_priest` : otro tipo de consulta o intenciones
    
Debes responder en formato JSON en la clave `retriever` el ítem detectado.
"""