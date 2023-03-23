from dataclasses import dataclass
from pos import Pos

@dataclass
class Item:
    name: str
    attack: int
    defence: int
    priority: int  
    pos: Pos
   
