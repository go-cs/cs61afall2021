'''
Author: your name
Date: 2022-01-20 14:38:30
LastEditTime: 2022-02-17 18:19:50
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Discussion\disc03.py
'''
#递归
def factorial(n):
    """Return the factorial of N, a positive integer."""
    if n == 1: # base case
        return 1
    else:      # Recursive call on a smaller problem.
        return n * factorial(n-1)

def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return m
    else :
        return m + multiply(m, n-1)


def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    # if n <= 1:
    #     return False
    # elif n == 2 or n == 3:
    #     return True
    # elif n % 2 == 0:
    #     return False
    # else:
    #     return is_prime(n-2)
    def helper(i):
        if i > (n ** 0.5):
            return True
        elif n % i == 0:
            return False
        return helper(i+1)
    return helper(2)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***" 
    print("%d"%(n))
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n/2)
    else:
        return 1 + hailstone(n*3+1)

def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    # n1, n2 are in decreasing order.
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 >= n2 % 10:
        return merge(n1//10,n2//10)*100 + (n1%10)*10+n2%10
    elif n1 % 10 < n2 % 10:
        return merge(n1//10,n2//10)*100 + (n2%10)*10+n1%10
    ## another solution
    # elif n1 % 10 < n2 % 10:
    #     return merge(n1 // 10, n2)*10 + n1 % 10
    # else:
    #     return merge(n1, n2 // 10)*10 + n2 % 10