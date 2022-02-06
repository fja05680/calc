from calc import node, TokenType


########################################################################
# PARSER - Implement the grammar using tokens from Lexer.
#
# Grammar:
#    expr             -> additive
#    additive         -> multiplicative ((PLUS | MINUS) multiplicative)*
#    multiplicative   -> unary (((MULTIPLY | DIVIDE ) unary) | LPAREN expr RPAREN)*
#    unary            -> (PLUS | MINUS) unary | exponential
#    exponential      -> primary POW exponential | primary
#    primary          -> NUMBER | LPAREN expr RPAREN
########################################################################

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.lookahead = None

    def _raise_error(self):
        raise Exception('Syntax error')

    def _match(self, token_type):
        ''' Get the next token. '''
        if (self.lookahead is not None and
            token_type == self.lookahead.token_type):
            try:
                self.lookahead = next(self.tokens)
            except StopIteration:
                self.lookahead = None
        else:
            self._raise_error()

    def _expr(self):
        return self._additive()

    def _additive(self):
        ''' Returns node "n". '''

        n = self._multiplicative()

        while self.lookahead is not None:
            if self.lookahead.token_type == TokenType.PLUS:
                self._match(TokenType.PLUS)
                n = node.Plus(n, self._multiplicative())
            elif self.lookahead.token_type == TokenType.MINUS:
                self._match(TokenType.MINUS)
                n = node.Minus(n, self._multiplicative())
            else:
                break
        return n


    def _multiplicative(self):
        n = self._unary()

        while self.lookahead is not None:
            if self.lookahead.token_type == TokenType.MULTIPLY:
                self._match(TokenType.MULTIPLY)
                n = node.Multiply(n, self._unary())
            elif self.lookahead.token_type == TokenType.DIVIDE:
                self._match(TokenType.DIVIDE)
                n = node.Divide(n, self._unary())
            elif self.lookahead.token_type == TokenType.LPAREN:
                self._match(TokenType.LPAREN)
                n = node.Multiply(n, self._expr())
                self._match(TokenType.RPAREN)
            else:
                break
        return n

    def _unary(self):
        if self.lookahead is not None:
            if self.lookahead.token_type == TokenType.PLUS:
                self._match(TokenType.PLUS)
                n = node.UPlus(self._unary())
            elif self.lookahead.token_type == TokenType.MINUS:
                self._match(TokenType.MINUS)
                n = node.UMinus(self._unary())
            else:
                n = self._exponential()
        return n

    def _exponential(self):
        n = self._primary()

        if self.lookahead is not None:
            if self.lookahead.token_type == TokenType.POW:
                self._match(TokenType.POW)
                n = node.Pow(n, self._exponential())
        return n


    def _primary(self):
        if self.lookahead is not None:
            if self.lookahead.token_type == TokenType.LPAREN:
                self._match(TokenType.LPAREN)
                n = self._expr()
                self._match(TokenType.RPAREN)
            elif self.lookahead.token_type == TokenType.NUMBER:
                n = node.Number(self.lookahead.value)
                self._match(TokenType.NUMBER)
            else:
                self._raise_error()

            return n

    def parse(self):
        ''' Returns the ROOT node of the tree. '''

        self.lookahead = next(self.tokens)

        if self.lookahead is None:
            return None

        root = self._expr()

        if self.lookahead is not None:
            self._raise_error()

        return root
