# The Collatz Sequence

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
