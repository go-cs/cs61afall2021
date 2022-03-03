'''
Author: your name
Date: 2022-01-25 19:33:33
LastEditTime: 2022-01-30 21:03:18
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Discussion\disc04.py
'''
from audioop import maxpp


def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_stair_ways(n-1) + count_stair_ways(n-2)


def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4) # 4, 3 + 1, 2 + 2, 2 + 1 +1, 1 + 1 + 2, 1 + 1 + 1 + 1, 1 + 3, 1 + 2+1
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    "*** YOUR CODE HERE ***"
    # if n < 0:
    #     return 0
    # if n == 0:
    #     return 1
    # if k == 1:
    #     return 1
    # return count_k(n-k, k) + count_k(n, k-1)

    if n < 0:
        return 0
    if n == 0: # 此处是为什么？为什么不是 n == 0 return 0
        return 1
    else:
        total, i = 0, 1
        while i <= k:
            total = total + count_k(n-i, k)
            i = i + 1
        return total


a = [1,5,4,[2,3],3]
print(a[0],a[-1])# 1 3
len(a)#5
2 in a #True. Error ,the answer is False
2 in a[3]#True
a[3][0] #2


def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i * s [i] for i in range(len(s)) if i % 2 == 0]

def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    # if len(s) == 0:
    #     return 1    
    # max_p = 1
    # for i in range(2, len(s)):
    #     product = 1
    #     for j in range(len(s[::i])):
    #         product = product * s[::i][j]
    #     if product > max_p:
    #         max_p = product
    # return max_p

    # another solution
    if s == []:
        return 1
    else :
        return max(max_product(s[1:]), s[0] * max_product(s[2:]))
