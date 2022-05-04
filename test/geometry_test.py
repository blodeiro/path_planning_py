import unittest
from path_planning_py.geometry import utils


class DistanceTest(unittest.TestCase):
    def setUp(self):
        self.func = utils.pointDistance

    def test_distance_1(self):
        p1 = [0,0,0]
        p2 = [5,0,0]
        self.assertEqual(
            self.func(p1,p2),
            5,
            "Points {} , {} distance incorrect".format(p1, p2)
            )

    def test_distance_2(self):
        p1 = [0,0,0]
        p2 = [1,0,0]
        self.assertEqual(
            self.func(p2,p1),
            1,
            "Points {} , {} distance incorrect".format(p2, p1)
            )

    def test_distance_3(self):
        p1 = [0,0,0]
        p3 = [1,1,0]
        self.assertAlmostEqual(
            self.func(p1,p3),
            1.41421,
            5,
            "Points {} , {} distance incorrect".format(p1, p3)
            )

    def test_distance_4(self):
        p1 = [0,0,0]
        p4 = [1,1,1]
        self.assertAlmostEqual(
            self.func(p1,p4),
            1.73205,
            5,
            "Points {} , {} distance incorrect".format(p1, p4)
            )


class NormalizeTest(unittest.TestCase):
    def setUp(self):
        self.func = utils.normalize

    def test_norm_1(self):
        p1 = [5,0,0]
        self.assertEqual(
            self.func(p1),
            [1,0,0]
            )
        
    def test_norm_1(self):
        p1 = [5,0,0]
        p2 = [5,5,0]
        self.assertEqual(
            self.func(p1,p2),
            [0,-1,0]
            )


class MoveTest(unittest.TestCase):
    def setUp(self):
        self.funcDir = utils.movePointDir
        self.funcTowards = utils.movePointTowards

    def test_dir_1(self):
        p1 = [5,0,0]
        direction = [0,0,1]
        distance = 10
        self.assertEqual(
            self.funcDir(p1,direction,distance),
            [5,0,10]
            )

    def test_tw_1(self):
        p1 = [5,0,0]
        target = [5,20,0]
        distance = 7
        self.assertEqual(
            self.funcTowards(p1,target,distance),
            [5,7,0]
            )

class CrossTest(unittest.TestCase):
    def setUp(self):
        self.funcDir = utils.crossDir

    def test_cross_1(self):
        u = [5,0,0]
        w = [0,20,0]
        result = [0,0,1]
        self.assertEqual(
            self.funcDir(u,w),
            result
            )

    def test_cross_2(self):
        u = [5,0,0]
        w = [0,20,0]
        result = [0,0,-1]
        self.assertEqual(
            self.funcDir(w,u),
            result
            )

class RotationTest(unittest.TestCase):
    def setUp(self):
        self.funcRot = utils.getRotMatrix

    def test_cross_1(self):
        direction = [5,0,0]
        result = [
            [1,0,0],
            [0,1,0],
            [0,0,1]
        ]
        self.assertEqual(
            self.funcRot(direction),
            result
            )

    def test_cross_1(self):
        direction = [0,5,0]
        result = [
            [0,1,0],
            [-1,0,0],
            [0,0,1]
        ]
        self.assertEqual(
            self.funcRot(direction),
            result
            )

if __name__ == '__main__':
    unittest.main()