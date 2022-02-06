#!/usr/bin/python3

import calc

def main():
    try:
        while True:
            try:
                expression = input('calc> ')

                # Parse the expression.
                lexer = calc.Lexer(expression)
                tokens = lexer.parse()
                print(tokens)
                parser = calc.Parser(tokens)
                tree = parser.parse()
                # Evaluate the expression.
                if tree:
                    value = tree.evaluate()
                    print(f'{tree} = {value}')
            except Exception as e:
                print(e)
    except KeyboardInterrupt:
        print()


if __name__ == '__main__':
    main()
