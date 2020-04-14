def factorial(n):
    if (n >= 1):
        return n * fact(n -1)
    else:
        return 1


# 
def fibonacci(n):
    if (n <= 0):
        return 0
    elif (n == 1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fib_memoized(n, memo):
    if memo[n] != None:
        return memo[n]
    else:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        result = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)
        memo[n] = result
        return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_memoized(n, memo)

def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

# print(factorial(0))
# print(fibonacci(10))
# print(fib_memo(6))
print(fib_bottom_up(9))

