import textparser
from textparser import Sequence


class Parser(textparser.Parser):

    def token_specs(self):
        return [
            ('SKIP',          r'[ \r\n\t]+'),
            ('WORD',          r'\w+'),
            ('EMARK',    '!', r'!'),
            ('COMMA',    ',', r','),
            ('MISMATCH',      r'.'),
            ('TRES', r'\"\"\"')
        ]

    def grammar(self):
        return Sequence('TRES', 'WORD', 'TRES')


tree = Parser().parse('\"\"\"Hello\"\"\"')

print('Tree:', tree)
