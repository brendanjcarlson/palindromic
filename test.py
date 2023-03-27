import unittest
from whiteboard import solution

class WhiteboardTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution('aaaabbbb'), True)

    def test_2(self):
        self.assertEqual(solution('abcdefg'), False)

    def test_3(self):
        self.assertEqual(solution('aabbccddeee'), True)

    def test_4(self):
        self.assertEqual(solution('aabbbccc'), False)

    def test_5(self):
        self.assertEqual(solution(''), False)

    def test_6(self):
        self.assertEqual(solution('zzz'), True)

if __name__ == '__main__':
    unittest.main()