# Find factorial of a number.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Print Fibonacci series up to n terms.

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print (a, end=' ')
        a, b = b, a + b

fibonacci(10)

def two_sum(nums, target):
    lookup={}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in lookup:
            return [lookup[diff], i]
        lookup[num] = i
    
print("sum of two",two_sum([2, 12,7, 11, 12], 9))