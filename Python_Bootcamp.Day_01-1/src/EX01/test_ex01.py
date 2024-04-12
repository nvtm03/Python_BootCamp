from ex01 import split_booty
from unittest import TestCase, main
from typing import Dict


class TestEX01(TestCase):
    test1: Dict[str, int] = {"gold_ingots": 3}
    test2: Dict[str, int] = {"gold_ingots": 2}
    test3: Dict[str, int] = {"apples": 10}
    test4: Dict[str, int] = {"trees": 20}
    test5: Dict[str, int] = {"gold_ingots": 10}
    test6: Dict[str, int] = {"gold_ingots": 2}
    test7: Dict[str, int] = {"gold_ingots": 4}

    def test_split_booty(self):
        self.assertTupleEqual(split_booty(self.test1, self.test2, self.test3, self.test4),
                              ({'gold_ingots': 2}, {'gold_ingots': 2}, {'gold_ingots': 1}))
        self.assertTupleEqual(split_booty(test1=self.test1, test2=self.test2, test3=self.test3, test4=self.test4),
                              ({'gold_ingots': 2}, {'gold_ingots': 2}, {'gold_ingots': 1}))
        self.assertTupleEqual(split_booty(self.test1, self.test2, test3=self.test3, test4=self.test4),
                              ({'gold_ingots': 2}, {'gold_ingots': 2}, {'gold_ingots': 1}))
        self.assertTupleEqual(split_booty(self.test1, self.test5, self.test6),
                              ({'gold_ingots': 5}, {'gold_ingots': 5}, {'gold_ingots': 5}))
        self.assertTupleEqual(split_booty(self.test7, self.test5, self.test6),
                              ({'gold_ingots': 6}, {'gold_ingots': 5}, {'gold_ingots': 5}))


if __name__ == '__main__':
    main()
