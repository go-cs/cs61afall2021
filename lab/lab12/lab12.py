'''
Author: your name
Date: 2022-03-01 16:00:15
LastEditTime: 2022-03-01 16:50:36
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \lab12\lab12.py
'''
import re


def calculator_ops(calc_str):
    """
    Finds expressions from the Calculator language that have two
    numeric operands and returns the expression without the parentheses.

    >>> calculator_ops("(* 2 4)")
    ['* 2 4']
    >>> calculator_ops("(+ (* 3 (+ (* 2 4) (+ 3 5))) (+ (- 10 7) 6))")
    ['* 2 4', '+ 3 5', '- 10 7']
    >>> calculator_ops("(* 2)")
    []
    """
    return re.findall(r"([+|\-|*|/]\s\d+\s\d+)", calc_str)
