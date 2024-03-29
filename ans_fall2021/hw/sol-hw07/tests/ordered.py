test = {
  'name': 'ordered?',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'setup': r"""
      scm> (load-all ".")
      """,
      'cases': [
        {
          'code': r"""
          scm> (ordered? '(1 2 3 4 5))  ; #t or #f
          #t
          """,
        },
        {
          'code': r"""
          scm> (ordered? '(1 5 2 4 3))  ; #t or #f
          #f
          """,
        },
        {
          'code': r"""
          scm> (ordered? '(2 2))  ; #t or #f
          #t
          """,
        },
        {
          'code': r"""
          scm> (ordered? '(1 2 2 4 3))  ; #t or #f
          #f
          """,
        },
      ],
    },
  ]
}