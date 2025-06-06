'''
Prblem = Last Digit of Fibonacci Number Problem

Compute the last digit of the n-th Fibonacci number.

    Input: An integer n.
    Output: The last digit of the n-th Fibonacci number.
'''


def fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
    
        previous, current = current, (previous + current)%10

    return current


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
