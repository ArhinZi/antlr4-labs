# Generated from calc.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("E\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\6\7\'\n\7\r\7")
        buf.write("\16\7(\3\b\3\b\3\t\3\t\3\n\7\n\60\n\n\f\n\16\n\63\13\n")
        buf.write("\3\n\3\n\6\n\67\n\n\r\n\16\n8\3\13\3\13\3\f\3\f\3\r\6")
        buf.write("\r@\n\r\r\r\16\rA\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\2\21\t\23\n\25\13\27\f\31\r\3\2\4\3\2\62;\5\2")
        buf.write("\13\f\17\17\"\"\2G\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3")
        buf.write("\2\2\2\5\35\3\2\2\2\7\37\3\2\2\2\t!\3\2\2\2\13#\3\2\2")
        buf.write("\2\r&\3\2\2\2\17*\3\2\2\2\21,\3\2\2\2\23\61\3\2\2\2\25")
        buf.write(":\3\2\2\2\27<\3\2\2\2\31?\3\2\2\2\33\34\7`\2\2\34\4\3")
        buf.write("\2\2\2\35\36\7,\2\2\36\6\3\2\2\2\37 \7\61\2\2 \b\3\2\2")
        buf.write("\2!\"\7-\2\2\"\n\3\2\2\2#$\7/\2\2$\f\3\2\2\2%\'\t\2\2")
        buf.write("\2&%\3\2\2\2\'(\3\2\2\2(&\3\2\2\2()\3\2\2\2)\16\3\2\2")
        buf.write("\2*+\7\60\2\2+\20\3\2\2\2,-\7.\2\2-\22\3\2\2\2.\60\t\2")
        buf.write("\2\2/.\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2")
        buf.write("\62\64\3\2\2\2\63\61\3\2\2\2\64\66\5\17\b\2\65\67\t\2")
        buf.write("\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2\29")
        buf.write("\24\3\2\2\2:;\7*\2\2;\26\3\2\2\2<=\7+\2\2=\30\3\2\2\2")
        buf.write(">@\t\3\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2BC\3")
        buf.write("\2\2\2CD\b\r\2\2D\32\3\2\2\2\7\2(\618A\3\b\2\2")
        return buf.getvalue()


class calcLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    POW = 1
    MUL = 2
    DIV = 3
    ADD = 4
    SUB = 5
    NUMBER = 6
    COMA = 7
    DECIMAL = 8
    LPAR = 9
    RPAR = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'^'", "'*'", "'/'", "'+'", "'-'", "','", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "POW", "MUL", "DIV", "ADD", "SUB", "NUMBER", "COMA", "DECIMAL", 
            "LPAR", "RPAR", "WS" ]

    ruleNames = [ "POW", "MUL", "DIV", "ADD", "SUB", "NUMBER", "SEP_DOT", 
                  "COMA", "DECIMAL", "LPAR", "RPAR", "WS" ]

    grammarFileName = "calc.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


