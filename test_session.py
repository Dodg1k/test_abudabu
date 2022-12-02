from unittest import TestCase, main
from session import circle_area
from math import pi


class TestCircleArea(TestCase):
    def test_area(self):
        self.assertEqual(circle_area(3), pi*3**2)
        self.assertEqual(circle_area(1), pi)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(2.5), pi*2.5**2)

    def test_values(self):
        self.assertRaises(ValueError, circle_area, -2)
        self.assertRaises(ValueError, circle_area, -12312)

    def test_type(self):
        self.assertRaises(TypeError, circle_area, 2 + 3j)
        self.assertRaises(TypeError, circle_area, 'one')
        self.assertRaises(TypeError, circle_area, [4])
        self.assertRaises(TypeError, circle_area, "Кукуруза")
        self.assertRaises(TypeError, circle_area, [7, 22])
        self.assertRaises(TypeError, circle_area, False)


# if __name__ == '__main__':
#     main()


