test = {
  'name': 'wwrm',
  'points': 0,
  'suites': [
    {
        'type': 'concept',
        'cases': [
        {
          'question': r"""#[a-f0-9]{6}""",
          'choices': ['Any 6-digit hexadecimal color code, like #fdb515', 'A hexadecimal color code that starts with letters and ends with numbers, like #gg1234', 'Any hexadecimal color code with 0-6 digits', 'A hexadecimal color code with 3 letters and 3 numbers'],
          'answer': 'Any 6-digit hexadecimal color code, like #fdb515',
        },
        {
          'question': r"""
          (fizz(buzz|)|buzz)
          """,
          'choices': ['Only fizzbuzz', 'Only fizz', 'Only fizzbuzz, fizz, and buzz', 'Only fizzbuzzbuzz', 'Only fizzbuzz or buzz'],
          'answer': 'Only fizzbuzz, fizz, and buzz',
        },
        {
          'question': r"""
          `[-+]?\d*\.?\d+`
          """,
          'choices': ['Signed or unsigned numbers like +1000, -1.5, .051', 'Only unsigned numbers like 0.051', 'Only signed numbers like +1000, -1.5',
          'Only signed or unsigned integers like +1000, -33'],
          'answer': 'Signed or unsigned numbers like +1000, -1.5, .051',
        }
      ]
    }
  ]
}