import random

from app.models.DataSheet import DataSheet


def roll_dices(num_dices: int) -> list[int]:
    return [random.randint(1, 6) for _ in range(num_dices)]

def calculate_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)

def can_charge(unit: DataSheet, target: DataSheet) -> bool:
    return unit["profile"]["movement"] >= target["profile"]["movement"]

def can_shoot(unit: dict, target: dict) -> bool:
    return unit["profile"]["save"] >= target["profile"]["save"]

def can_move(unit: dict, target: dict) -> bool:
    return unit["profile"]["movement"] >= target["profile"]["movement"]

def can_attack(unit: dict, target: dict) -> bool:
    return unit["profile"]["save"] >= target["profile"]["save"]

def can_use_ability(unit: dict, ability: str) -> bool:
    return unit["abilities"]["core"].lower() == ability.lower()