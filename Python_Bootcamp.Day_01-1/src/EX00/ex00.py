from typing import Dict


def add_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    return {'gold_ingots': purse.get('gold_ingots', 0) + 1}


def empty(purse: Dict[str, int]) -> Dict[str, int]:
    return {}


def get_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    ingots: int | None = purse.get('gold_ingots', None)
    if ingots is None or ingots <= 0:
        return {}
    return {'gold_ingots': ingots - 1}
