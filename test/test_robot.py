import unittest
from path_planning_py.robot import robot


class DistanceTest(unittest.TestCase):
    def setUp(self):
        self.robot = robot.Robot({})

    def test_move_1(self):
        self.assertEqual(
            self.robot.move(),
            True,
            )
    def test_move_2(self):
        self.robot.addWaypoint([5,0,0])
        self.robot.addWaypoint([17,0,0])
        self.assertEqual(
            self.robot.move(),
            True,
            )
    def test_move_2(self):
        self.robot.addWaypoint([30,0,0])
        self.robot.addWaypoint([30,2,2])
        self.robot.addWaypoint([30,2,20])
        self.assertEqual(
            self.robot.move(),
            True,
            )


if __name__ == '__main__':
    unittest.main()