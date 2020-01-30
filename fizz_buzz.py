#fizz buzz function that handles only positive integers

def fizz_buzz(x):
    if(type(x) == int and x > 0):
        if(x % 3 == 0 and x % 5 == 0):
            return 'FizzBuzz'
        elif(x % 3 == 0):
            return 'Fizz'
        elif(x % 5 == 0):
            return 'Buzz'
        return x
    return 'Please enter a positive integer'

#print first 100 numbers for fizz buzz or up to another defined limit

number = 1
limit = 100

while number <= limit:
    print(fizz_buzz(number))
    number += 1