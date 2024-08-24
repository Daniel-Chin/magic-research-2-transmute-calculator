from shared import *
from mr_types import *

def shard(name: str, element: Element):
    return Item(name, .29, [
        (mana, 5), 
        (element, 500), 
    ])

def prism(name: str, element: Element):
    return Item(name, 1.2, [
        (mana, 50),
        (element, 50 * K),
    ])

fireShard = shard("fireShard", fire)
earthShard = shard("earthShard", earth)
waterShard = shard("waterShard", water)
airShard = shard("airShard", air)
poisonShard = shard("poisonShard", poison)
mindShard = shard("mindShard", mind)
lifeShard = shard("lifeShard", life)
elecShard = shard("elecShard", elec)
timeShard = shard("timeShard", time)
deathShard = shard("deathShard", death)

firePrism = prism("firePrism", fire)
earthPrism = prism("earthPrism", earth)
waterPrism = prism("waterPrism", water)
airPrism = prism("airPrism", air)
poisonPrism = prism("poisonPrism", poison)
mindPrism = prism("mindPrism", mind)
lifePrism = prism("lifePrism", life)
elecPrism = prism("elecPrism", elec)
timePrism = prism("timePrism", time)
deathPrism = prism("deathPrism", death)
