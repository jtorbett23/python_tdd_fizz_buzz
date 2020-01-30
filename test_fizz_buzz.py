import unittest
import fizz_buzz

class Test_fizz_buzz(unittest.TestCase):
    #returns a number
    def test_number(self):
        self.assertEqual(fizz_buzz.fizz_buzz(1),1)
    #returns Fizz on multiples of 3
    def test_fizz(self):
        self.assertEqual(fizz_buzz.fizz_buzz(3),'Fizz')
        self.assertEqual(fizz_buzz.fizz_buzz(42),'Fizz')
    #returns Buzz on multiples of 5
    def test_buzz(self):
        self.assertEqual(fizz_buzz.fizz_buzz(5),'Buzz')
        self.assertEqual(fizz_buzz.fizz_buzz(65),'Buzz')
    #returns FizzBuzz on multiples of 3 & 5
    def test_buzz(self):
        self.assertEqual(fizz_buzz.fizz_buzz(15),'FizzBuzz')
        self.assertEqual(fizz_buzz.fizz_buzz(90),'FizzBuzz')


    
    

#to allow to run tests in terminal with 'python test_fizz_buzz.py'
if __name__ == '__main__':
    unittest.main()