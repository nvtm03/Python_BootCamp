from typing import Iterable
from itertools import zip_longest


def fix_wiring(cables: Iterable, sockets: Iterable, plugs: Iterable) -> str:
    cables = list(filter(lambda x: isinstance(x, str), cables))
    sockets = list(filter(lambda x: isinstance(x, str), sockets))
    plugs = list(filter(lambda x: isinstance(x, str), plugs))
    while len(sockets) == len(cables) != len(plugs):
        plugs.append(404)
    for cable, socket, plug in zip(cables, sockets, plugs):
        yield f'weld {cable} to {socket} without plug' if plug == 404 else f'plug {cable} into {socket} using {plug}'

# one line
# def fix_wiring(cables: Iterable, sockets: Iterable, plugs: Iterable):
#     return [f'weld {csp[0]} to {csp[1]} without plug' if csp[2] == 404 else f'plug {csp[0]} into {csp[1]} using {csp[2]}' for csp in zip_longest(*map(lambda lst: list(filter(lambda x: isinstance(x, str), lst)), [cables, sockets, plugs]), fillvalue=404) if csp[0] != 404 and csp[1] != 404]


def test():
    # test 1
    plugs_1 = ['plug1', 'plug2', 'plug3']
    sockets_1 = ['socket1', 'socket2', 'socket3', 'socket4']
    cables_1 = ['cable1', 'cable2', 'cable3', 'cable4']
    assert list(fix_wiring(cables_1, sockets_1, plugs_1)) == ['plug cable1 into socket1 using plug1',
                                                              r'plug cable2 into socket2 using plug2',
                                                              'plug cable3 into socket3 using plug3',
                                                              'weld cable4 to socket4 without plug']

    # test 2
    plugs_2 = ['plugZ', None, 'plugY', 'plugX']
    sockets_2 = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables_2 = ['cable2', 'cable1', False]
    assert list(fix_wiring(cables_2, sockets_2, plugs_2)) == ['plug cable2 into socket1 using plugZ',
                                                              'plug cable1 into socket2 using plugY']


if __name__ == '__main__':
    test()
