'''
Author: your name
Date: 2022-02-24 19:30:31
LastEditTime: 2022-02-24 20:52:35
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Discussion\disc11.py
'''
class Pair:
    """Represents the built-in pair data structure in Scheme."""
    def __init__(self, first, rest):
        from scheme_builtins import scheme_valid_cdrp, SchemeError
        self.first = first
        if not scheme_valid_cdrp(rest):
            raise SchemeError("cdr can only be a pair, nil, or a promise but was {}".format(rest))
        self.rest = rest

    def map(self, fn):
        """Maps fn to every element in a list, returning a new
        Pair.

        >>> Pair(1, Pair(2, Pair(3, nil))).map(lambda x: x * x)
        Pair(1, Pair(4, Pair(9, nil)))
        """
        assert isinstance(self.rest, Pair) or self.rest is nil, \
            "rest element in pair must be another pair or nil"
        return Pair(fn(self.first), self.rest.map(fn))

    def __repr__(self):
        return 'Pair({}, {})'.format(self.first, self.rest)


class nil:
    """Represents the special empty pair nil in Scheme."""
    def map(self, fn):
        return nil
    def __getitem__(self, i):
         raise IndexError('Index out of range')
    def __repr__(self):
        return 'nil'

nil = nil() # this hides the nil class *forever*

def calc_eval(exp):
    if isinstance(exp, Pair): # Call expressions
        return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif exp in OPERATORS:      # Names
        return OPERATORS[exp]
    else:                       # Numbers
        return exp
def floor_div(expr):
    "*** YOUR CODE HERE ***"
    dividend = expr.first
    expr = expr.rest
    while expr.rest != nil:
        divisor = expr.first
        dividend //= divisor
        exp = exp.rest
    return dividend


# Assume OPERATORS['//'] = floor_div is added for you in the code


def calc_eval(exp):
    if isinstance(exp, Pair):
        if exp.first == 'and': # and expressions
            return eval_and(exp.rest)
        else:                   # Call expressions
            return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif exp in OPERATORS:      # Names
        return OPERATORS[exp]
    else:                       # Numbers
        return exp

def eval_and(operands):
    "*** YOUR CODE HERE ***"
    # if operands == False:
    #     return False
    # return operands
    curr, val = operands, True
    while curr is not nil:
        val = calc_eval(curr.first)
        if val is False:
            return False
        curr = curr.rest
    return val

bindings = {}
def calc_eval(exp):
    if isinstance(exp, Pair):
        if exp.first == 'and': # and expressions[paste your answer from the earlier]
            return eval_and(exp.rest)
        elif exp.first == 'define': # define expressions
            return eval_define(exp.rest)

        else:                   # Call expressions
            return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif exp in bindings: # Looking up variables
        "*** YOUR CODE HERE ***"
        return bindings[exp]
    elif exp in OPERATORS:      # Looking up procedures
        return OPERATORS[exp]
    else:                       # Numbers
        return exp

def eval_define(expr):
    "*** YOUR CODE HERE ***"
    name, value = expr.first, calc_eval(expr.rest.first)
    bindings[name] = value
    return name




