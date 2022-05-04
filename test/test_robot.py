import unittest
from path_planning_py.robot import robot


class DistanceTest(unittest.TestCase):
    def setUp(self):
        self.robot = robot.Robot({})

    def test_hello(self):
        self.assertEqual(
            self.robot.hello(),
            "hello",
            )


if __name__ == '__main__':
    unittest.main()