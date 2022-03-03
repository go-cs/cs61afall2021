'''
Author: your name
Date: 2022-01-09 18:50:12
LastEditTime: 2022-01-09 19:14:42
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \sp21\interleave.py
'''
def interleave_digits(a,b):
    """Assuming A and B are non-negative integers with the same number 
    of base-10 digits,return the number whose base-10 representation is 
    the interleaving of A's and B's digits,starting with A.
    >>> interleave_digits(1, 2)
    12
    >>> interleave_digits(0, 1)
    1
    >>> interleave_digits(1, 0)
    10
    >>> interleave_digits(123,456)
    142536
    """
    if a <= 9:
        return a * 10 + b
    return interleave_digits(a // 10, b // 10) * 100 + interleave_digits(a % 10, b % 10)


if __name__ == '__main__':
    import doctest
    doctest.testmod()