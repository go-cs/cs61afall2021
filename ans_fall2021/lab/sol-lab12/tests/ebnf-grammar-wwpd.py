test = {
  'name': 'ebnf-grammar',
  'points': 0,
  'suites': [
    {
        'type': 'concept',
        'cases': [
        {
          'question': r"""
          Which aspects of the Calculator language are supported by this grammar?
          """,
          'choices': ['The subtraction operator requires at least one argument.',
                      'The division operator requires at least two arguments.',
                      'Each of the operands can itself be a Calculator expression.',
                      'Variables can be defined and used as operands.'],
          'answer': 'Each of the operands can itself be a Calculator expression.',
        },
        {
          'question': r"""
          Which of the following expressions would NOT be parsable according to that BNF?
          """,
          'choices': ['(+ 1 2)', '(+)', '(+ 1 2 3)', '(+ 1)', '(1 + 2)', '(+ 1 (+ 2 3))'],
          'answer': '(1 + 2)',
        },
        {
          'question': r"""
          Which line of the BNF should we modify to add support for calculations using a modulus operator, like (% 15 5)?
          """,
          'choices': ['start: calc_expr',
                      '?calc_expr: NUMBER | calc_op',
                      'calc_op: "(" OPERATOR calc_expr* ")"',
                      'OPERATOR: "+" | "-" | "*" | "/"'],
          'answer':  'OPERATOR: "+" | "-" | "*" | "/"',
        },
        {
          'question': r"""
         Does the BNF grammar provide enough information to create a working interpreter for this version of the Calculator language?
          """,
          'choices': ['Yes, if we feed this grammar into a program that understands BNF grammars, it will be able to parse Calculator expressions and output the result.',
                      'Yes, but only if we feed this grammar into a program that was written in the Calculator language itself.',
                      'No, this grammar gives enough information for parsing a Calculator expression, but it does not provide enough information to evaluate it.',
                      'No, this grammar does not provide enough information for the parsing or evaluation step, it is useful mostly as documentation.'],
          'answer': 'No, this grammar gives enough information for parsing a Calculator expression, but it does not provide enough information to evaluate it.',
        }
      ]
    }
  ]
}