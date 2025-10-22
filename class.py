from enum import Enum
from random import randint

class UnitAbility(Enum):
    ANTI_FIGHTER_BARRAGE = 1
    BOMBARDMENT = 2
    DEPLOY = 3
    PLANETARY_SHIELD = 4
    SPACE_CANNON = 5
    SUSTAIN_DAMAGE = 6
    NEGATE_PDS = 7
    

# The following are a list of classes for TI4:TE Combat Calculator
class Unit:
    def __init__(self,name:str, type:str = "", abilities: list[UnitAbility]=[], attack_num: int = -1, attack_value: int = -1) -> None:
        # Passed Variables
        self.name = name
        self.type = name
        self.abilities = abilities
        self.attack_num = attack_num
        self.attack_value = attack_value
        # Internally Kept Variables
        self.status = 1 # 1 is alive, 0 is dead
        self.id = 1 # Keeps Track of the Unit number, Dread 1, Dread 2, etc.
        self.hits = 0 # How many hits are rolled during the current combat round.
    
    def __repr__(self) -> str:
        return f"{self.name} {self.id}"
    
    def roll(self):
        if self.attack_value != -1 or self.attack_num != -1:
            for i in range(self.attack_num):
                if randint(1,10) >= self.attack_value:
                    self.hits += 1   
        else:
            self.hits = 0

    
class UnitList:
    def __init__(self, player:str) -> None:
        self.player = player
        # Lists of Units
        self.fighterList = []
        self.destroyerList = []
        self.cruiserList = []
        self.carrierList = []
        self.dreadnoughtList = []
        self.warSunList = []
        self.infantryList = []
        self.mechList = []
        self.spaceDockList = []
        self.pdsList = []
    
    def set_ID(self,unitList:list):
        for u in unitList:
            u.id = unitList.index(u) + 1
    
    def add(self, unit: Unit):
        if unit.name == "Fighter":
            self.fighterList.append(unit)
            self.set_ID(self.fighterList)
        if unit.name == "Destroyer":
            self.destroyerList.append(unit)
            self.set_ID(self.destroyerList)
        if unit.name == "Cruiser":
            self.cruiserList.append(unit)
            self.set_ID(self.cruiserList)
        if unit.name == "Carrier":
            self.carrierList.append(unit)
            self.set_ID(self.carrierList)
        if unit.name == "Dreadnought":
            self.dreadnoughtList.append(unit)
            self.set_ID(self.dreadnoughtList)
        if unit.name == "War Sun":
            self.warSunList.append(unit)
            self.set_ID(self.warSunList)
        if unit.name == "Infantry":
            self.infantryList.append(unit)
            self.set_ID(self.infantryList)
        if unit.name == "Mech":
            self.mechList.append(unit)
            self.set_ID(self.mechList)
        if unit.name == "Space Dock":
            self.spaceDockList.append(unit)
            self.set_ID(self.spaceDockList)
        if unit.name == "PDS":
            self.pdsList.append(unit)
            self.set_ID(self.pdsList)
