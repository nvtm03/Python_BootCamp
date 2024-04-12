from unittest import TestCase, main
from ex00 import add_ingot, empty, get_ingot
from typing import Dict


class TestEX00(TestCase):
    test1: Dict[str, int] = {}
    test2: Dict[str, int] = {'gold_ingots': 13}
    test3: Dict[str, int] = {'gold_ingots': 0}
    test4: Dict[str, int] = {'gold_ingots': -1}
    test5: Dict[str, int] = {'gold_ingots': -100}

    def test_add_ingot(self):
        self.assertDictEqual(add_ingot(self.test1), {'gold_ingots': 1})
        self.assertDictEqual(add_ingot(self.test2), {'gold_ingots': 14})

    def test_empty(self):
        self.assertDictEqual(empty(self.test1), {})

    def test_get_ingot(self):
        self.assertDictEqual(get_ingot(self.test1), {})
        self.assertDictEqual(get_ingot(self.test3), {})
        self.assertDictEqual(get_ingot(self.test4), {})
        self.assertDictEqual(get_ingot(self.test5), {})
        self.assertDictEqual(get_ingot(self.test2), {'gold_ingots': 12})


if __name__ == '__main__':
    main()
