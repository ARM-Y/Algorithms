# Maximum Pairwise Product Problem
#
# Find the maximum product of two distinct numbers in a sequence of non-negative integers.
#
# Input:
#   n: An integer representing the number of integers in the sequence.
#   sequence: A list or array of n non-negative integers.
#
# Output:
#   The maximum value that can be obtained by multiplying two different elements from the sequence.
#
# Example:
#   Input:
#     n = 3
#     sequence = [1, 2, 3]
#   Output:
#     6 (obtained by multiplying 3 and 2)
#
# Example:
#   Input:
#     n = 5
#     sequence = [10, 3, 14, 2, 7]
#   Output:
#     140 (obtained by multiplying 14 and 10)
#
# Constraints:
#   - n >= 2 (The sequence will have at least two numbers)
#   - 0 <= sequence[i] (All numbers in the sequence are non-negative)


def max_pairwise_product(numbers):
    
    # finding the first maximum
    # intializing 
    first_Max = numbers[0] 
    first_Max_index = 0
    
    # finding 1_Max
    for index in range(1,len(numbers)):
        if first_Max < numbers[index]:
            first_Max = numbers[index]
            first_Max_index = index

    # finding the second maximum
    # intializing 
    if first_Max_index != 0:
        second_Max = numbers[0] 
    else: 
        second_Max = numbers[1] 
    #second_Max_index = 0
    
    # finding 1_Max
    for index in range(1,len(numbers)):
        if second_Max < numbers[index] and index != first_Max_index :
            second_Max = numbers[index]
            #second_Max_index = index

    return second_Max*first_Max



if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))

