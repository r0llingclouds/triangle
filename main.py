from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def main():
    while True:
        try:
            text = input('calc> ')
            if not text:
                continue
            lexer = Lexer(text)
            parser = Parser(lexer)
            interpreter = Interpreter(parser)
            result = interpreter.interpret()
            print(result)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
