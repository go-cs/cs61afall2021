test = {
  'name': 'regex_grouping',
  'points': 1,
  'suites': [
    {
      'type': 'lark',
      'cases': [
        {
          'locked': False,
          'code': r"""
          lark> r"col(o|(ou))r"
          rstring
            word  col
            group
              pipe
                character  o
                group
                  word  ou
            character  r
          lark> r"apples|oranges"
          rstring
            pipe
              word  apples
              word  oranges
          """,
        },
      ],
      'scored': True,
      'setup': r"""
      %import hw10 (rstring, word, group, pipe, class, character, range, num_quant, plus_quant, star_quant)
      %ignore /\s+/
      ?start: rstring
      """,
    },
  ]
}