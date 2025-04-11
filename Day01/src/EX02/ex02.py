from typing import Dict


def squeak(func):
    def wrapper(*args, **kwargs):
        print('SQUEAK')
        return func(*args, **kwargs)
    return wrapper


@squeak
def add_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    return {'gold_ingots': purse.get('gold_ingots', 0) + 1}


@squeak
def empty(purse: Dict[str, int]) -> Dict[str, int]:
    return {}


@squeak
def get_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    ingots: int | None = purse.get('gold_ingots', None)
    if ingots is None or ingots <= 0:
        return {}
    return {'gold_ingots': ingots - 1}
