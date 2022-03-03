'''
Author: your name
Date: 2022-01-09 17:18:31
LastEditTime: 2022-01-09 18:45:40
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \sp21\reverse_eg.py
'''
def reverse_digit(n):
    """Assuming N >= 0 is an integer.  Return the number whose bse-10 representation is the
    reverse of that of N.
    >>> reverse_digit(0)
    0
    >>> reverse_digit(1)
    1
    >>> reverse_digit(123)
    321
    >>> reverse_digit(10)
    1
    >>> reverse_digit(12321)
    12321
    >>> reverse_digit(201)
    102
    >>> reverse_digit(2222)
    2222
    """
    assert type(n) is int and n >= 0
    if n < 10:
        return n
    return reverse_digit(n // 10) + (n % 10) * 10**(num_digit(n)-1)
def num_digit(x):
    """Return the number of decimal digits in the positive integer X."""
    x_count = 1
    while x>=10:
        x_count+=1
        x //= 10
    return x_count



if __name__ == '__main__':
    import doctest
    doctest.testmod()