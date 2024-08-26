from shared import *
from mr_types import *
from basics_items import *
from more_items import *

def reduceDict(a: tp.Dict, b: tp.Dict):
    for k, v in b.items():
        a[k] = a.get(k, 0.0) + v

def factoryOf(item: Item, n: float = 1):
    jobs: tp.Dict[Item, float] = {item: n}
    raws: tp.Dict[Raw, float] = {}
    for resource, amount in item.cost:
        unit_per_sec = amount * n / item.sec_per_transmute
        del amount
        if isinstance(resource, Raw):
            raws[resource] = raws.get(resource, 0) + unit_per_sec
        elif isinstance(resource, Item):
            subjobs, subraws = factoryOf(
                resource, 
                unit_per_sec * resource.sec_per_transmute, 
            )
            reduceDict(jobs, subjobs)
            reduceDict(raws, subraws)
        else:
            assert False, type(resource)
    return jobs, raws

def display(jobs: tp.Dict[Item, float], raws: tp.Dict[Raw, int]):
    print('Wizard assignments:')
    for item, amount in jobs.items():
        print(item.name, format(amount, '.2f'), sep='\t')
    print()
    print('Raw:')
    for raw, amount in raws.items():
        print(raw.name, format(amount, '.2f'), sep='\t')

def main():
    jobs = {}
    raws = {}
    def f(item: Item, amount: int):
        j, r = factoryOf(item, amount)
        reduceDict(jobs, j)
        reduceDict(raws, r)
    f(alchemistsCowl, 10)
    f(tamersWand, 10)
    f(ringOfRagingFamiliar, 10)
    f(potionOfAccuracy, 10)
    f(potionOfSharpness, 10)
    f(greaterPotionOfMuscle, 10)
    f(greaterPotionOfToughness, 10)
    display(jobs, raws)

if __name__ == "__main__":
    main()
