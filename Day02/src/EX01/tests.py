from ex01 import *


def test_default_game() -> None:
    # test1
    game = Game()
    game.game()
    assert game.registry == {'copycat': 57, 'grudger': 46, 'cheater': 45, 'detective': 45, 'cooperator': 29}


def test_game_with_my_type() -> None:
    # test2
    game = Game()
    game.game((Copycat(), Cheater(), Cooperator(), Grudger(), Detective(), MyBehavioralType()))
    assert game.registry == {'copycat': 75, 'detective': 63, 'my_type': 58, 'grudger': 51, 'cooperator': 46,
                             'cheater': 45}


def test_default_game_100_matches() -> None:
    # test3
    game = Game(100)
    game.game()
    assert game.registry == {'copycat': 597, 'detective': 495, 'grudger': 406, 'cheater': 315, 'cooperator': 209}


def test_game_with_my_type_100_matches() -> None:
    # test4
    game = Game(100)
    game.game((Copycat(), Cheater(), Cooperator(), Grudger(), Detective(), MyBehavioralType()))
    assert game.registry == {'copycat': 795, 'detective': 693, 'my_type': 598, 'grudger': 411, 'cooperator': 406,
                             'cheater': 315}


if __name__ == '__main__':
    test_default_game()
    test_game_with_my_type()
    test_default_game_100_matches()
    test_game_with_my_type_100_matches()
