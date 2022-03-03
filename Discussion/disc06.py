'''
Author: your name
Date: 2022-02-09 19:16:19
LastEditTime: 2022-02-09 21:06:53
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Discussion\disc06.py
'''
s1 = [1, 2, 3]
s2 = s1
s1 is s2#True
print('=================')
s2.extend([5, 6])#s2 = [1, 2, 3, 5, 6]
s1[4]#s1 = [1, 2, 3, 5, 6]， s1与s2指向同一块位置
print('=================')
s1.append([-1, 0, 1])#[-1, 0, 1]整体视为一个元素，所以不会报错
s2[5]#[-1, 0, 1]
print('==================')
s3 = s2[:]#复制 s3 = [1, 2, 3, 5, 6, [-1, 0, 1]]
s3.insert(3, s2.pop(3))#s3 = [1, 2, 3, 5, ,5,  6, [-1, 0, 1]],是s2.pop(3)
#s3.insert(3, s3.pop(3))#则s3没有变化
len(s1)
print('=================')
#s1 = [1, 2, 3, 6, [-1, 0, 1]]
#s3 = [1, 2, 3, 5, 5, 6, [-1, 0, 1]]
s1[4] is s3[6]#True s1[4] == [-1, 0, 1]
print('==============')
s3[s2[4][1]]# s3[0] = 1
print('==============')
s1[:3] == s2[:3]#True
print('==============')
s1[4].append(2)#s1[4] = [-1, 0, 1, 2]
s3[6][3]


def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs in s.
    #把el添加到列表s的末尾，次数是x在s中出现的次数
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for elem in s:
        if elem == x:
            count = count + 1
    while count > 0:
        s.append(el)
        count -= 1


def countdown(n):
    print("Beginning countdown!")
    while n >= 0:
        yield n
        n -= 1
    print("Blastoff!")


def filter_iter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    "*** YOUR CODE HERE ***"
    #return iter([x for x in iterable if fn(x)])
    for x in iterable:
        if fn(x):
            yield x

def sequence(start, step):
        while True:
            yield start
            start += step
            
def merge(a, b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    "*** YOUR CODE HERE ***"
    
    s_a = next(a)
    s_b = next(b)
    while True:
        if s_a < s_b:
            yield s_a
            s_a = next(a)
        elif s_a == s_b:
            yield s_a
            s_a = next(a)
            s_b = next(b)
        else:
            yield s_b
            s_b = next(b)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n == 1:
        return 
    if is_prime(n):
        yield n
    yield from primes_gen(n - 1)

def mystery(p, q):
    p[1].extend(q)
    q.append(p[1:])

p = [2, 3]
q = [4, [p]]
mystery(q, p)


