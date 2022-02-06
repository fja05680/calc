from enum import Enum
import string

########################################################################
# Character Sets
########################################################################

WhitespaceSet = ' \t\n'
NumberSet     = string.digits + '.'


########################################################################
# Tokens
########################################################################

class TokenType(Enum):
    NUMBER    = 0
    PLUS      = 1
    MINUS     = 2
    MULTIPLY  = 3
    DIVIDE    = 4
    LPAREN    = 5
    RPAREN    = 6
    POW       = 7


class Token:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value

    def __repr__(self):
        return f"{self.token_type} {self.value if self.value else ''}"


########################################################################
# LEXER - Generate list of tokens from the input string.
########################################################################


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.lookahead = None
        self.tokens = []

    def _raise_error(self):
        raise Exception(f"Invalid character '{self.lookahead}'")

    def _get_next_char(self):
        try:
            self.lookahead = next(self.text)
        except StopIteration:
            self.lookahead = None

    def _parse_number(self):
        ''' Returns a Number token. '''

        number_str = self.lookahead
        self._get_next_char()

        while self.lookahead is not None and self.lookahead in NumberSet:
            number_str += self.lookahead
            self._get_next_char()

        num_decimal_points = number_str.count('.')
        value = None

        if num_decimal_points == 0:
            value = int(number_str)
        elif num_decimal_points == 1:
            value = float(number_str)
        else:
            raise Exception('Invalid number format')

        return Token(TokenType.NUMBER, value)

    def _parse_multiply(self):
        multiply_str = self.lookahead
        self._get_next_char()

        while self.lookahead is not None and self.lookahead == '*':
            multiply_str += self.lookahead
            self._get_next_char()

        num_multiply_chars = multiply_str.count('*')
        if num_multiply_chars == 1:
            return Token(TokenType.MULTIPLY)
        elif num_multiply_chars == 2:
            return Token(TokenType.POW)
        else:
            raise Exception('Invalid multiply format')

    def parse(self):
        ''' Returns a list of tokens. '''

        self._get_next_char()
        while self.lookahead != None:
            if self.lookahead in WhitespaceSet:
                pass
            elif self.lookahead in NumberSet:
                self.tokens.append(self._parse_number())
                continue
            elif self.lookahead == '+':
                self.tokens.append(Token(TokenType.PLUS))
            elif self.lookahead == '-':
                self.tokens.append(Token(TokenType.MINUS))
            elif self.lookahead == '*':
                self.tokens.append(self._parse_multiply())
                continue
            elif self.lookahead == '/':
                self.tokens.append(Token(TokenType.DIVIDE))
            elif self.lookahead == '(':
                self.tokens.append(Token(TokenType.LPAREN))
            elif self.lookahead == ')':
                self.tokens.append(Token(TokenType.RPAREN))
            else:
                self._raise_error()

            self._get_next_char()
        return self.tokens
