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
    #returns an error message for non-positive integers
    def test_edge_cases(self):
        # 0 and negative integers
        self.assertEqual(fizz_buzz.fizz_buzz(0),'Please enter a positive integer')
        self.assertEqual(fizz_buzz.fizz_buzz(-1),'Please enter a positive integer')
        self.assertEqual(fizz_buzz.fizz_buzz(-5),'Please enter a positive integer')
        #float values
        self.assertEqual(fizz_buzz.fizz_buzz(0.5),'Please enter a positive integer')
        self.assertEqual(fizz_buzz.fizz_buzz(-2.5),'Please enter a positive integer')
        #character values
        self.assertEqual(fizz_buzz.fizz_buzz('1'),'Please enter a positive integer')
        self.assertEqual(fizz_buzz.fizz_buzz('a'),'Please enter a positive integer')
        


    
    

#to allow to run tests in terminal with 'python test_fizz_buzz.py'
if __name__ == '__main__':
    unittest.main()