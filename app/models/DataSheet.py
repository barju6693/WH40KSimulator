from pydantic import BaseModel, Field, field_validator
from enum import Enum

class Hability(BaseModel):
    name: str = Field(description="")
    description: str = Field(description="")

class WargearAbilities(BaseModel):
    name: str
    description: str

class Abilities(BaseModel):
    core: str = Field(description="")
    faction: str = Field(description="")
    habilities_list: list[Hability] = Field(description="")
    invulnerable_save: str = Field(description="")


class WeaponsType(str, Enum):
    ranged = "ranged"
    melee = "melee"


class Weapons(BaseModel):
    weapons_type: WeaponsType
    range: int
    attacks: int
    weapon_skill: int
    ballistic_skill: int
    strength: int
    armour_penetration: int
    damage: int

    @field_validator("range", mode="before")
    def check_range(cls,v, values):
        if values["weapons_type"] == WeaponsType.ranged:
            return v
        else:
            return 0



class Keywords(str, Enum):
    infantry = "Infantry"
    character = "Character"
    epic_hero = "Epic hero"
    terminator = "Terminator"
    chapter_master = "Chapter master"
    logan_grimnar = "Logan Grimnar"
    battleline = "Battleline"
    grenades = "Grenades"
    imperium = "Imperium"
    grey_hunters = "Grey hunters"
    blood_claws = "Blood claws"



class FactionKeywords(str, Enum):
    adeptus_astartes = "Adeptus Astartes"
    space_wolves = "Space Wolves"
    black_templars = "Black Templars"
    dark_angels = "Dark Angels"
    chaos_demons = "Chaos Daemons"
    space_marines = "Space Marines"
    grey_knights = "Grey Knights"


class WargearOptions(BaseModel):
    what_repleced: str = Field(description="")
    oprtion: dict[str, int]


class UnitComposition(BaseModel):
    amount_min: int
    amount_max: int
    name: str
    description: str
    attached_unit: str


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
    Abilities: Abilities = Field(description="")
    weapons: list[Weapons] = Field(description="")
    faction_keywords: list[FactionKeywords] = Field(description="")
    keywords: list[Keywords] = Field(description="")
    unit_composition: UnitComposition = Field(description="")
    wargear_options: WargearOptions = Field(description="")
