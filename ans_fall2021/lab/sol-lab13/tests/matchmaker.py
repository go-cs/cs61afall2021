test = {
  'name': 'matchmaker',
  'points': 1,
  'suites': [
    {
      'type': 'sqlite',
      'setup': """
      sqlite> .read lab13.sql
      """,
      'cases': [
        {
            'code': r"""
            sqlite> SELECT * FROM matchmaker LIMIT 10;
            dog|Clair De Lune|blue|green
            dog|Clair De Lune|blue|purple
            dog|Clair De Lune|blue|blue
            dog|Clair De Lune|blue|space gray
            dog|Clair De Lune|blue|green
            dog|Clair De Lune|blue|black
            dog|Clair De Lune|blue|green
            dog|Clair De Lune|blue|blue
            dog|Clair De Lune|blue|blue
            dog|Clair De Lune|blue|blue
            """,
          'hidden': False,
          'locked': False
        }
      ],
    }
  ]
}