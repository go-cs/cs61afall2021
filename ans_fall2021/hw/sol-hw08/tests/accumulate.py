test = {
  'name': 'accumulate',
  'points': 1,
  'suites': [
    {
      'scored': True,
      'setup': """
      scm> (load-all ".")
      scm> (define (identity x) x)
      """,
      'type': 'scheme',
      'cases': [
        {
          'code': """
          scm> (accumulate * 1 5 identity)
          120
          """,
          'hidden': False,
        },
      ],
    },
    {
      'type': 'scheme',
      'setup': """
      scm> (load-all ".")
      """,
      'cases': [
        {
          'code': """
          scm> (define (square x) (* x x))
          square
          scm> (accumulate + 0 5 square)
          55
          scm> (accumulate + 5 5 square)
          60
          """,
          'hidden': False
        }
      ],
    },
  ]
}