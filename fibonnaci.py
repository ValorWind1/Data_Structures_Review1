# fibonacci sequence is a series of numbers wheere a number is found by adding two numbers before..

""" Did this one recursively """
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))


""" Note from book : Memoization- dynamic programing """

def mfib(n,memo):
    if memo[n] is not None: # checing if memo[n] is empty / or if we already have seen it
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    else :
        result = mfib(n-1,memo) + mfib(n-2,memo)
    memo[n] = result
    return result


def memo_fib(n):
    memo = [None] * (n+1)
    return mfib(n,memo)

print(memo_fib(10))

