class Key:
    passphrase = 'zax2rulez'

    def __len__(self):
        return 1337

    def __str__(self):
        return 'GeneralTsoKeycard'

    def __gt__(self, other):
        return True

    def __getitem__(self, item):
        return 3


def tests():
    key = Key()
    assert len(key) == 1337
    assert key[404] == 3
    assert key > 9000
    assert key.passphrase == "zax2rulez"
    assert str(key) == "GeneralTsoKeycard"


if __name__ == '__main__':
    tests()
