import unittest
from fina.code_challenges.wolf_in_sheeps_clothing.wolf_in_sheeps_clothing import warn_the_sheep


class MyTestWolfCase(unittest.TestCase):

    def test_method_exists(self):
        sheep_wolf_queue = ['sheep']
        self.assertFalse(warn_the_sheep(sheep_wolf_queue=sheep_wolf_queue))

    def test_when_wolf_in_front_of_line(self):
        expected_value = 'Pls go away'
        sheep_wolf_queue = ['sheep', 'wolf']
        actual_value = warn_the_sheep(sheep_wolf_queue=sheep_wolf_queue)

        self.assertEqual(expected_value, actual_value)

    def test_when_wolf_not_in_front_of_line(self):
        expected_value = 'Oi! Sheep 2, wolf is behind you!'
        sheep_wolf_queue = ['wolf', 'sheep', 'sheep']
        actual_value = warn_the_sheep(sheep_wolf_queue=sheep_wolf_queue)

        self.assertEqual(expected_value,actual_value)

    def test_when_wolf_in_the_middle(self):
        sheep_wolf_queue = ['sheep', 'wolf', 'sheep']
        expected_value = 'Oi! Sheep 1, wolf is behind you!'
        actual_value = warn_the_sheep(sheep_wolf_queue=sheep_wolf_queue)

        self.assertEqual(expected_value,actual_value)

#todo: fill out following tests
    def test_when_wolf_in_the_middle_two_wolfs(self):
        sheep_wolf_queue = ['sheep', 'wolf', 'wolf', 'sheep']
        expected_value = 'Oi! Sheep 1, wolf is behind you!' #todo
        actual_value = warn_the_sheep(sheep_wolf_queue=sheep_wolf_queue)

        self.assertEqual(expected_value,actual_value)

    def test_when_wolf_alternating_two_wolfs(self):
        sheep_wolf_queue = ['wolf', 'sheep', 'wolf', 'sheep']
        expected_value = 'Oi! Sheep 1, wolf is behind you!' #todo
        actual_value = warn_the_sheep(sheep_wolf_queue=sheep_wolf_queue)

        self.assertEqual(expected_value,actual_value)

    def test_no_wolf(self):
        sheep_wolf_queue = ['sheep', 'sheep']
        expected_value = 'Oi! Sheep 1, wolf is behind you!' #todo
        actual_value = warn_the_sheep(sheep_wolf_queue=sheep_wolf_queue)

        self.assertEqual(expected_value,actual_value)

    def test_no_sheep_only_wolf(self):
        sheep_wolf_queue = ['wolf']
        expected_value = 'Oi! Sheep 1, wolf is behind you!' #todo
        actual_value = warn_the_sheep(sheep_wolf_queue=sheep_wolf_queue)

        self.assertEqual(expected_value,actual_value)

    def test_other_animal(self):
        sheep_wolf_queue = ['lion']
        expected_value = 'Oi! Sheep 1, wolf is behind you!' #todo
        actual_value = warn_the_sheep(sheep_wolf_queue=sheep_wolf_queue)

        self.assertEqual(expected_value,actual_value)


if __name__ == '__main__':
    unittest.main()
