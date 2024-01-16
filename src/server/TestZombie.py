import unittest
from unittest.mock import MagicMock
from Zombie import Zombie
from Referee import Referee
from random import seed

class TestZombie(unittest.TestCase):
    def setUp(self):
        self.referee_mock = MagicMock(spec=Referee)
        self.zombie = Zombie(self.referee_mock, "Zombie1")

    def test_wander_returns_new_position(self):
        seed(42)

        # Mock the initial position
        self.referee_mock.range = {"Zombie1": {'x': 5, 'y': 7}}

        # Call the wander method
        new_position = self.zombie.wander()

        # Check that the returned position is a tuple of length 2
        self.assertIsInstance(new_position, tuple)
        self.assertEqual(len(new_position), 2)

        # Check if x and y are valid
        x_posible_positions = [4, 5, 6]
        y_posible_positions = [6, 7, 8]
        self.assertIn(new_position[0], x_posible_positions)
        self.assertIn(new_position[1], y_posible_positions)

    def test_get_position(self):
        self.referee_mock.range = {"Zombie1": {'x': 2, 'y': 3}}
        position = self.zombie.get_position()
        self.assertEqual(position, (2, 3))

if __name__ == '__main__':
    unittest.main()
