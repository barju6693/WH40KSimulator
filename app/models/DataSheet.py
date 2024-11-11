from pydantic import BaseModel, Field
from enum import Enum


class Habilities(BaseModel):
    pass


class WeaponsType(str, Enum):
    ranged = "ranged"
    melee = "melee"


class Weapons(BaseModel):
    range = int
    attacks = int
    weapon_skill = int
    ballistic_skill = int
    strength = int
    armour_penetration = int
    damage = int


class Keywords(str, Enum):
    pass

class FactionKeywords(str, Enum):
    pass


class WargearOptions(BaseModel):
    pass


class UnitComposition(BaseModel):
    pass


class Profiles(BaseModel):
    movement: int = Field(description="")
    resistence: int = Field(description="")
    salvation: int = Field(description="")
    save: int = Field(description="")
    wounds: int = Field(description="")
    leadership: int = Field(description="")
    objective_control: int = Field(description="")


class DataSheet(BaseModel):
    name: str = Field(description="")
    profile: Profiles = Field(description="")
    habilities: Habilities = Field(description="")
    weapons: list[Weapons] = Field(description="")
    faction_keywords: list[FactionKeywords] = Field(description="")
    keywords: list[Keywords] = Field(description="")
    unit_composition: UnitComposition = Field(description="")
    wargear_options: WargearOptions = Field(description="")
