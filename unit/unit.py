import unittest

from OO.OOSr import Student



class TestStudent(unittest.TestCase):
    def test_init(self):
        s = Student()
        self.assertEquals(s.score,0)

    def test_say(self):
        s = Student()
        self.assertEquals(s.say,'Hello world')


