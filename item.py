from dataclasses import dataclass

from pos import Pos


@dataclass
class Item:
    name: str
    priority: int 
    pos: Pos
    attack: int
    defence: int