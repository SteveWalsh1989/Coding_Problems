
"""

Write a program that prints the numbers from 1 to n.

- for multiples of three print “Fizz” instead of the number 
- for the multiples of five print “Buzz”. 
- for numbers which are multiples of both three and five print “FizzBuzz”."



"""


def fizz_buzz(n):
    # Write your code here

    for i in range(1, n + 1):

        if i % 3 == 0 and i % 5 == 0:
            print(f"FizzBuzz")
        elif i % 3 == 0 and i % 5 != 0:
            print(f"Fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print(f"Buzz")
        elif i % 5 != 0 or i % 3 != 0:
            print(i)
            
            
def main():
    """ Main function"""
  
    n = 15
    fizz_buzz(n)


''' Run Program '''
main()