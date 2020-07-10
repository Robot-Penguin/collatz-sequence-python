# The Collatz Sequence

# The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: 
# start with any positive integer n. 
# Then each term is obtained from the previous term as follows: 
# if the previous term is even, the next term is one half of the previous term. 
# If the previous term is odd, the next term is 3 times the previous term plus 1. 
# The conjecture is that no matter what value of n, the sequence will always reach 1. 
# - Wikipedia

def collatz(number):
    remainder = number % 2
    if remainder == 0:
        number = number // 2
        print(number)
        return number
    else:
        number = 3 * number + 1
        print(number)
        return number
  
print('Enter number:')
number = int(input())

collatz_sequence = collatz(number)

while collatz_sequence != 1:
    collatz_sequence = collatz(collatz_sequence)
