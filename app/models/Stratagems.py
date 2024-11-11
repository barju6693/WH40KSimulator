from pydantic import BaseModel
from enum import Enum

class StatagemKey(str, Enum):
    either_player_turn = "either_player_turn"
    my_turn = "my_turn"
    opponent_turn = "opponent_turn"

class StratagemCategory(str, Enum):
    battle_tactic = "battle_tactic"
    epic_deed = "epic_deed"
    strategic_deployment = "strategic_deployment"
    wargear = "wargear"

class Stratagem(BaseModel):
    name: str
    description: str
    when: str
    target: str
    effect: str