import unittest
from yuri_manga_processing.preprocessing import mappings


class MyTestCase(unittest.TestCase):
    def test_numeric_of_completed_is_equal_const(self):
        result = mappings.from_user_reading_status_to_numeric("completed")
        self.assertEqual(result, mappings.COMPLETED_INDEX)

    def test_numeric_of_plan_to_read_is_equal_const(self):
        result = mappings.from_user_reading_status_to_numeric("plan_to_read")
        self.assertEqual(result, mappings.PLAN_TO_READ_INDEX)


if __name__ == '__main__':
    unittest.main()
