from random import randint


def shoot(self):
    return 'Shooting'


def search(self):
    return 'Searching'


def talk(self):
    return 'Talking'


def turrets_generator():
    # generate personality traits
    neuroticism = randint(0, 100)
    openness = randint(0, 100 - neuroticism)
    conscientiousness = randint(0, 100 - neuroticism - openness)
    extraversion = randint(0, 100 - neuroticism - openness - conscientiousness)
    agreeableness = 100 - neuroticism - openness - conscientiousness - extraversion

    attributes = {
        'neuroticism': neuroticism,
        'openness': openness,
        'conscientiousness': conscientiousness,
        'extraversion': extraversion,
        'agreeableness': agreeableness,
        'shoot': shoot,
        'search': search,
        'talk': talk
    }
    yield type('Turret', (object,), attributes)()


def tests():
    Turret = next(turrets_generator())

    # test attributes
    assert 0 <= Turret.neuroticism <= 100
    assert 0 <= Turret.openness <= 100
    assert 0 <= Turret.conscientiousness <= 100
    assert 0 <= Turret.extraversion <= 100
    assert 0 <= Turret.agreeableness <= 100
    assert (Turret.neuroticism + Turret.openness + Turret.conscientiousness
            + Turret.extraversion + Turret.agreeableness == 100)

    # test methods
    assert Turret.shoot() == 'Shooting'
    assert Turret.search() == 'Searching'
    assert Turret.talk() == 'Talking'


if __name__ == '__main__':
    tests()
