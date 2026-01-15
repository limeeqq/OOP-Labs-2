import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Domain.student import Student
    #aaa
class TestStudent(unittest.TestCase):
    def setUp(self):
        self.s = Student("Test", "User", 3, "KB1", "15-07-2005", "IP")

    def test_create(self):
        self.assertEqual(self.s.course, 3)

    def test_transfer(self):
        self.s.transfer()
        self.assertEqual(self.s.course, 4)

    def test_transfer_limit(self):
        self.s.course = 6
        self.s.transfer()
        self.assertEqual(self.s.course, 6)

    def test_summer_true(self):
        self.assertTrue(self.s.is_summer())

    def test_summer_false(self):
        self.s.birth_date = "01-01-2005"
        self.assertFalse(self.s.is_summer())

if __name__ == '__main__': unittest.main()