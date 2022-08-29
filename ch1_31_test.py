from unittest import TestCase
from ch1_31 import guar_win


class P31a(TestCase):
    c1 = {"numpool": 5, "slots": 3, "win_thresh": 2}

    def setUp(self):
        self.gw = guar_win(**self.__class__.c1)

    def test_gw_pos(self):
        self.assertTrue(self.gw({1, 2, 3}, {2, 3, 4}, {3, 4, 5}))
        self.assertTrue(self.gw({1, 2, 3}, {1, 4, 5}))

    def test_gw_neg(self):
        self.assertFalse(self.gw({1, 2, 3}))
        self.assertFalse(self.gw({1, 2, 3}, {1, 2, 4}))


class P31b(TestCase):
    c1 = {"numpool": 6, "slots": 3, "win_thresh": 2}

    def setUp(self):
        self.gw = guar_win(**self.__class__.c1)

    def test_gw_pos(self):
        self.assertTrue(self.gw({1, 2, 3}, {2, 3, 4}, {3, 4, 5}))
        self.assertTrue(self.gw({1, 2, 3}, {1, 4, 5}))

    def test_gw_neg(self):
        self.assertFalse(self.gw({1, 2, 3}))
        self.assertFalse(self.gw({1, 2, 3}, {1, 2, 4}))