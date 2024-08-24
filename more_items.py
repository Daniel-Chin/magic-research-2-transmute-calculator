from shared import *
from mr_types import *
from basics_items import *

thickHide = Item("thickHide", 2, [
    (mana, 500), 
    (earth, 1 * M), 
    (earthShard, 3), 
])

cotton = Item("cotton", 24, [
    (mana, 600),
    (air, 18 * K), 
])

ruggedLeatherArmor = Item("ruggedLeatherArmor", 24, [
    (mana, 1300),
    (earth, 1 * M),
    (firePrism, 50),
    (earthPrism, 25),
    (thickHide, 500),
])

potionOfAccuracy = Item("potionOfAccuracy", 24, [
    (mana, 500),
    (mind, 20 * K),
    (poison, 20 * K),
    (waterShard, 3),
    (mindShard, 25),
])

potionOfSharpness = Item("potionOfSharpness", 24, [
    (mana, 500),
    (elec, 30 * K),
    (poison, 30 * K),
    (waterShard, 3),
    (elecShard, 18),
])

potionOfEvasion = Item("potionOfEvasion", 24, [
    (mana, 600),
    (air, 30 * K),
    (poison, 20 * K),
    (waterShard, 3),
    (airShard, 25),
    (poisonShard, 10),
])

greaterPotionOfMuscle = Item("greaterPotionOfMuscle", 24, [
    (mana, 1800),
    (fire, 5 * M),
    (firePrism, 100),
    (poisonPrism, 20),
    (slimeDrop, 500),
])

thunderWhip = Item("thunderWhip", 24, [
    (mana, 1300),
    (elec, 2 * M),
    (elecPrism, 50),
    (magicSalt, 8),
])

evasiveGarb = Item("evasiveGarb", 24, [
    (mana, 400),
    (air, 25 * K),
    (airShard, 25),
    (cotton, 8), 
])

cloakOfDarkness = Item("cloakOfDarkness", 24, [
    (mana, 400), 
    (air, 15 * K), 
    (airShard, 15),
    (cotton, 2),
])

alchemistsCowl = Item("alchemistsCowl", 24, [
    (mana, 1600),
    (poison, 3 * M),
    (poisonPrism, 150),
    (cotton, 50),
])
