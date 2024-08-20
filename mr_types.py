from __future__ import annotations

import typing as tp
from dataclasses import dataclass

class Resource: pass

@dataclass(frozen=True)
class Raw(Resource):
    name: str

mana = Raw('Mana')
coin = Raw('Coin')

class Element(Raw): pass
fire   = Element('Fire')
earth  = Element('Earth')
water  = Element('Water')
air    = Element('Air')
poison = Element('Poison')
mind   = Element('Mind')
life   = Element('Life')
elec   = Element('Elec')
time   = Element('Time')
death  = Element('Death')

@dataclass(frozen=True)
class Item(Resource):
    name: str
    sec_per_transmute: float
    cost: tp.List[tp.Tuple[Resource, int]]

    def __hash__(self):
        return hash(self.name)

slimeDrop = Raw('SlimeDrop')
