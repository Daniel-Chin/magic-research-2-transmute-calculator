from shared import *
from mr_types import *
from basics_items import *

thickHide = Item("thickHide", 2.65, [
    (mana, 500), 
    (earth, 1 * M), 
    (earthShard, 3), 
])

ruggedLeatherArmor = Item("ruggedLeatherArmor", 31.8, [
    (mana, 1300),
    (earth, 1 * M),
    (firePrism, 50),
    (earthPrism, 25),
    (thickHide, 500),
])

potionOfAccuracy = Item("potionOfAccuracy", 31.8, [
    (mana, 500),
    (mind, 20 * K),
    (poison, 20 * K),
    (waterShard, 3),
    (mindShard, 25),
])

potionOfSharpness = Item("potionOfSharpness", 31.8, [
    (mana, 500),
    (elec, 30 * K),
    (poison, 30 * K),
    (waterShard, 3),
    (elecShard, 18),
])

potionOfEvasion = Item("potionOfEvasion", 31.8, [
    (mana, 600),
    (air, 30 * K),
    (poison, 20 * K),
    (waterShard, 3),
    (airShard, 25),
    (poisonShard, 10),
])

greaterPotionOfMuscle = Item("greaterPotionOfMuscle", 31.8, [
    (mana, 1800),
    (fire, 5 * M),
    (firePrism, 100),
    (poisonPrism, 20),
    (slimeDrop, 500),
])
