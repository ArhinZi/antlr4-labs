from antlr4 import *
from calcLexer import calcLexer
from evalVisitor import evalVisitor
from calcParser import calcParser
import sys



def main():
    lexer = calcLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = calcParser(stream)
    tree = parser.expr()
    eval = evalVisitor()
    print(eval.visit(tree))


if __name__ == '__main__':
    main()