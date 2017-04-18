import string
import random


def generateGradesDict(_length):
    _grades = {}
    while True:
        _name = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
        _A = random.randrange(0, 101)
        _B = random.randrange(0, 101)
        _C = random.randrange(0, 101)
        _D = random.randrange(0, 101)
        _E = random.randrange(0, 101)
        _grades[_name] = (int)((_A+_B+_C+_D+_E)/5)
        if (len(_grades) == _length):
            break
    return _grades
