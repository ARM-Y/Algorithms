# Problem Definition: (Fibonacci Number Problem):
# Compute the n-th Fibonacci number.
#
# Input:
#   n: An integer representing the index of the desired Fibonacci number (n >= 0).
#
# Output:
#   The n-th Fibonacci number.
#
# Definition of Fibonacci numbers:
#   F(0) = 0
#   F(1) = 1
#   F(n) = F(n-1) + F(n-2) for n > 1
#
# Examples:
#   Input:
#     n = 0
#   Output:
#     0

#   Input:
#     n = 10
#   Output:
#     55

def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        fibonacci_number_list = [0,1]
        for i in range(n):
            fibonacci_number_list.append(fibonacci_number_list[-1]+fibonacci_number_list[-2])

    return fibonacci_number_list[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
