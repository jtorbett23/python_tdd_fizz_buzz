import unittest
import fizz_buzz

class Test_fizz_buzz(unittest.TestCase):
    #returns a number
    def test_number(self):
        self.assertEqual(fizz_buzz.fizz_buzz(1),1)

#to allow to run tests in terminal with 'python test_fizz_buzz.py'
if __name__ == '__main__':
    unittest.main()