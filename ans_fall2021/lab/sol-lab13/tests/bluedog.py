test = {
  'name': 'bluedog',
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
          sqlite> SELECT * FROM bluedog;
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          blue|dog
          sqlite> SELECT * FROM bluedog_songs;
          blue|dog|Clair De Lune
          blue|dog|Shake It Off
          blue|dog|Old Town Road
          blue|dog|Dancing Queen
          blue|dog|Old Town Road
          blue|dog|Clair De Lune
          blue|dog|Dancing Queen
          blue|dog|Clair De Lune
          blue|dog|STAY
          blue|dog|Old Town Road
          blue|dog|Shake It Off
          blue|dog|STAY
          blue|dog|Clair De Lune
          blue|dog|Clair De Lune
          blue|dog|STAY
          blue|dog|Clair De Lune
          """,
        },
      ],
    },
  ]
}