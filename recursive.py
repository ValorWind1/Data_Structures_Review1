
""" Recursion: breaks the problem into smaller problems , and calls itself for each of the smaller problems."""

# --------------------------------------------------------------------------------------------------------------

""" An iterative Algorithm : the iterative solution uses a loop and computes as it goes
Iterative = A Loop """

# recursive algorithm
# sudo code
# function getFactorial(n)
    #if n < 2 , return 1  # this means that if n is equal to 1 or 2 return 1
    # else return n * getFactorial(n-1)  # def : otherwise return the n times of n-1.

""" Recursion Pros & Cons """
# may run out of memory we have to open millions of recursive calls ( requires more memory)
# more abstract/ harder to understand than iterative solutions

# --------------

# in some cases extremely fast and easy to code, and practical for tree traversal and binary search


""" Factorial Recursively """

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))
print(factorial(2))
print(factorial(0))

""" Factorial Iteratively """

def ifactorial(n):
    if n < 0:
        return -1
    else:
        factor = 1
        for i in range(1,n+1):
            factor *= i
        return factor

print(ifactorial(5))
print(ifactorial(2))
print(ifactorial(0))
