# Set A : Problem 1

#The task is to count the total number of suits in the list using both iterative and recursive approaches.
# No, the problem explicitly states not to use the len() function for counting.

def count_suits_iterative(suits):
    total = 0
    for suit in suits:
        if suit:
            total += 1
    return total

def count_suits_recursive(suits):
    # Base case: if the list is empty, return 0
    if not suits:
        return 0
    else:
    # Recursive case: Return 1 plus the result of a recursive call to the same function with the rest of the list (excluding the first item).
        return 1 + count_suits_recursive(suits[1:])


print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))


# Problem 2

def sum_stones(stones):
    if not stones:
        return 0
    # Recursive case: Return the first stone's value plus the sum of the rest of the stones.
    else:
        return stones[0] + sum_stones(stones[1:])


print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))


# Problem 3

def count_suits_iterative(suits):
    unique = set()
    for suit in suits:
        if suit:
            unique.add(suit)
    return len(unique)

def count_suits_recursive(suits):
    # Base case
    if not suits:
        return 0
    # Recursive case
    else:
        first = suits[:1]
        rest = suits[1:]
        if first[0] in rest:
            return count_suits_recursive(rest)
        else:
            return 1 + count_suits_recursive(rest)



print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

#--------------------------------------------------------------------------------------------------
# Binary Search:
# Time complexity: O(log n)
# Space complexity: O(1) for iterative, O(log n) for recursive due to recursion stack
def binary_search(numbers, value):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] > value:
            high = mid - 1  # Move the high pointer to the left of the mid index
        elif numbers[mid] < value:
            low = mid + 1  # Move the low pointer to the right of the mid index
        else:
            return mid

    return None


# Merge Sort:
# Time complexity: O(n log n)
# Space complexity: O(n) for the merged array
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: arrays with 1 or no elements are already sorted

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = 0  # Pointer for left half
    j = 0  # Pointer for right half

    # Compare elements from both halves and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements in the left or right half
    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Fibonacci Sequence:
# Time complexity: O(2^n) for naive recursion, O(n) for memoization or iterative approach
# Space complexity: O(n) for memoization, O(1)
def fib(n, cache):
    if cache is None:
        cache = {0: 0, 1: 1}
        
    if n in cache:
        return cache[n]
    
    cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
    return cache[n]

print(fib(40, None))  # Example usage, calculating the 40th Fibonacci number

# The Call Stack:
# The call stack is a data structure that stores information about the active subroutines of a computer program.
# It is used to keep track of function calls, local variables, and the point of execution in a program.
# Each time a function is called, a new frame is added to the stack, and when the function returns, that frame is removed.
# This allows for recursive function calls to be managed, as each call has its own context and local variables.
# Time complexity: O(n) for the number of function calls, where n is the depth of recursion
# Space complexity: O(n) for the call stack depth in recursive calls
def function_c():
    print("I'm Function C!")
    print("Function C is done executing!")

def function_b():
    print("I'm Function B!")
    function_c()
    print("Function B is done executing!")

def function_a():
    print("I'm Function A!")
    function_b()
    print("Function A is done executing!")

function_a()
#--------------------------------------------------------------------------------------------------

