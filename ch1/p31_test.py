from unittest import TestCase
from ch1.p31 import guar_win, gen_tix_v1, gen_tix_v2


class GuarWin(TestCase):
    c1 = {"numpool": 5, "slots": 3, "win_thresh": 2}

    def setUp(self):
        self.gw = guar_win(**self.__class__.c1)

    def test_pos(self):
        self.assertTrue(self.gw({1, 2, 3}, {2, 3, 4}, {3, 4, 5}))
        self.assertTrue(self.gw({1, 2, 3}, {1, 4, 5}))

    def test_neg(self):
        self.assertFalse(self.gw({1, 2, 3}))
        self.assertFalse(self.gw({1, 2, 3}, {1, 2, 4}))


class GenTix(TestCase):
    c1 = {"numpool": 5, "slots": 3, "win_thresh": 2}

    def setUp(self):
        self.gw = guar_win(**self.__class__.c1)

    def test_correct(self):
        self.assertTrue(self.gw(*gen_tix_v1(**self.__class__.c1)))
        self.assertTrue(self.gw(*gen_tix_v2(**self.__class__.c1)))

