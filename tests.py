from unittest import TestCase

from args import parse_args


# python args.py --verbose --count=2 run
# {
#   "--verbose": True,
#   "--count": 2,
#   "[]": ["run"],
# }

class ArgsTestCase(TestCase):

    def test_option_with_equals(self):
        args = parse_args(['--name=bob'])
        self.assertEqual(args['--name'], 'bob')

        args = parse_args(['--first=jane', '--last=austin'])
        self.assertEqual(args['--first'], 'jane')
        self.assertEqual(args['--last'], 'austin')

    def test_option_with_integer_value(self):
        args = parse_args(['--count=2'])
        self.assertEqual(args['--count'], 2)

    def test_flag(self):
        args = parse_args(['--verbose'])
        self.assertTrue(args['--verbose'])

        args = parse_args(['--verbose', '--name=bob'])
        self.assertTrue(args['--verbose'])
        self.assertEqual(args['--name'], 'bob')

    def test_command(self):
        args = parse_args(['bob'])
        self.assertEqual(args['[]'], ["bob"])
