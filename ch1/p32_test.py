from random import randint, choice
from unittest import TestCase
from ch1.p32 import intdiv


class IntDiv(TestCase):
    def testFunc(self):
        for _ in range(100):
            x, y = (randint(-50, 50), choice(list(set(range(-50, 51)) - {0})))
            with self.subTest((x, y)):
                self.assertEqual(intdiv(x, y), x // y)
