test = {
  'name': 'avg-difference',
  'points': 1,
  'suites': [
    {
      'type': 'sqlite',
      'setup': """
      sqlite> .read lab13.sql
      """,
      'cases': [
        {
          'locked': False,
          'code': r"""
          sqlite> SELECT * FROM avg_difference;
          543.0
          """,
        },
      ],
    },
  ]
}