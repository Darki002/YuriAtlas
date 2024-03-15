import unittest
import LevensteinsDistance


class MyTestCase(unittest.TestCase):
    def test_returns_expected_distance(self):

        result = LevensteinsDistance.distance("book", "back")

        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
