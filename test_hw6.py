import unittest

class TestDisciplineGame(unittest.TestCase):
    def test_task_reached(self):
        self.assertEqual(check_task_completion(3, 2), True)

    def test_task_failed(self):
        self.assertEqual(check_task_completion(1, 2), False)

    def test_format_lowercase(self):
        self.assertEqual(format_furniture_name("sofa"), "Sofa")

    def test_format_uppercase(self):
        self.assertEqual(format_furniture_name("BED"), "Bed")

if __name__ == '__main__':
    unittest.main()
