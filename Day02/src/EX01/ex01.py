from collections import Counter


class Game(object):
    def __init__(self, matches=10) -> None:
        self.matches: int = matches
        self.registry: Counter = Counter()

    def play(self, player1, player2) -> None:
        """
        simulate number of matches
        :param player1:
        :param player2:
        """

        moves: dict[str, list] = {'player1': [], 'player2': []}
        for _ in range(self.matches):
            player1_decision: bool = player1.decision(moves['player2'])
            player2_decision: bool = player2.decision(moves['player1'])
            moves['player1'].append(player1_decision)
            moves['player2'].append(player2_decision)
            self.__coin_toss(player1_decision, player2_decision, player1, player2)

    def __coin_toss(self, player1_decision, player2_decision, player1, player2) -> None:
        if player1_decision is True and player2_decision is True:
            self.registry[str(player1)] = self.registry.get(str(player1), 0) + 2
            self.registry[str(player2)] = self.registry.get(str(player2), 0) + 2
        elif player1_decision is False and player2_decision is True:
            self.registry[str(player1)] = self.registry.get(str(player1), 0) + 3
            self.registry[str(player2)] = self.registry.get(str(player2), 0) - 1
        elif player1_decision is True and player2_decision is False:
            self.registry[str(player1)] = self.registry.get(str(player1), 0) - 1
            self.registry[str(player2)] = self.registry.get(str(player2), 0) + 3

    def game(self, behavior_types=None) -> None:
        """default game"""
        if behavior_types is None:
            behavior_types = (Copycat(), Cheater(), Cooperator(), Grudger(), Detective())
        for i in range(len(behavior_types)):
            for j in range(i + 1, len(behavior_types)):
                self.play(behavior_types[i], behavior_types[j])
        self.top3()

    def top3(self) -> None:
        """ print top 3 players """

        sorted_players: list[tuple[str, int]] = sorted(self.registry.items(), key=lambda x: (-int(x[1]), x[0]))

        for i in range(3):
            print(f'{sorted_players[i][0]} {sorted_players[i][1]}')


class Player:
    def __init__(self, name='player') -> None:
        self.__name: str = name

    def decision(self, opponent_moves) -> bool | None:
        return None

    def __str__(self):
        return self.__name


class Cheater(Player):
    def __init__(self):
        super().__init__('cheater')

    def decision(self, opponent_moves):
        return False


class Cooperator(Player):
    def __init__(self):
        super().__init__('cooperator')

    def decision(self, opponent_moves):
        return True


class Copycat(Player):
    def __init__(self):
        super().__init__('copycat')

    def decision(self, opponent_moves):
        if opponent_moves:
            return opponent_moves[-1]
        return True


class Grudger(Player):
    def __init__(self):
        super().__init__('grudger')

    def decision(self, opponent_moves):
        if False in opponent_moves:
            return False
        return True


class Detective(Player):
    def __init__(self):
        super().__init__('detective')

    first_four_moves: tuple[bool, bool, bool, bool] = (True, False, True, True)

    def decision(self, opponent_moves):
        if len(opponent_moves) < 4:
            return self.first_four_moves[len(opponent_moves)]
        if False in opponent_moves:
            return opponent_moves[-1]
        return False


class MyBehavioralType(Player):
    def __init__(self):
        super().__init__('my_type')

    def decision(self, opponent_moves: list[bool]) -> bool | None:
        if len(opponent_moves) < 1:
            return False
        if opponent_moves.count(False) > opponent_moves.count(True):
            return False
        return True


def main() -> None:
    print('----test1----\n'
          'Players: Copycat, Cheater, Cooperator, Grudger, Detective\n'
          'matches: 10\n'
          '-------------')
    game = Game()
    game.game()

    print('\n----test2----\n'
          'Players: Copycat, Cheater, Cooperator, Grudger, Detective, MyBehavioralType\n'
          'matches: 10\n'
          '-------------')
    game = Game()
    game.game((Copycat(), Cheater(), Cooperator(), Grudger(), Detective(), MyBehavioralType()))

    print('\n----test3----\n'
          'Players: Copycat, Cheater, Cooperator, Grudger, Detective\n'
          'matches: 100\n'
          '-------------')
    game = Game(100)
    game.game()

    print('\n----test4----\n'
          'Players: Copycat, Cheater, Cooperator, Grudger, Detective, MyBehavioralType\n'
          'matches: 100\n'
          '-------------')
    game = Game(100)
    game.game((Copycat(), Cheater(), Cooperator(), Grudger(), Detective(), MyBehavioralType()))


if __name__ == '__main__':
    main()
