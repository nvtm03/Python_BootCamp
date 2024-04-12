from typing import Tuple, Dict


def split_booty(*args, **kwargs) -> Tuple[Dict[str, int], Dict[str, int], Dict[str, int]]:
    all_ingots: int = sum(arg.get('gold_ingots', 0) for arg in args)
    all_ingots += sum(kwarg.get('gold_ingots', 0) for kwarg in kwargs.values())

    return_value: int = all_ingots // 3
    if all_ingots % 3 == 0:
        return {"gold_ingots": return_value}, {"gold_ingots": return_value}, {"gold_ingots": return_value}
    if all_ingots % 3 == 1:
        return {"gold_ingots": return_value + 1}, {"gold_ingots": return_value}, {"gold_ingots": return_value}
    return {"gold_ingots": return_value + 1}, {"gold_ingots": return_value + 1}, {"gold_ingots": return_value}
