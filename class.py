from enum import Enum

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
    def __init__(self,name:str, abilities: list[UnitAbility], attack_num: int, attack_value: int) -> None:
        # Passed Variables
        self.name = name
        self.abilities = abilities
        self.attack_num = attack_num
        self.attack_value = attack_value
        # Internally Kept Variables
        self.status = 1 # 1 is alive, 0 is dead
        self.id = 1 # Keeps Track of the Unit number, Dread 1, Dread 2, etc.
    
    def __repr__(self) -> str:
        return f"{self.name} {self.id}"