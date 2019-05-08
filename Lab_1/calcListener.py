# Generated from calc.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .calcParser import calcParser
else:
    from calcParser import calcParser

# This class defines a complete listener for a parse tree produced by calcParser.
class calcListener(ParseTreeListener):

    # Enter a parse tree produced by calcParser#prog.
    def enterProg(self, ctx:calcParser.ProgContext):
        pass

    # Exit a parse tree produced by calcParser#prog.
    def exitProg(self, ctx:calcParser.ProgContext):
        pass


    # Enter a parse tree produced by calcParser#Dec.
    def enterDec(self, ctx:calcParser.DecContext):
        pass

    # Exit a parse tree produced by calcParser#Dec.
    def exitDec(self, ctx:calcParser.DecContext):
        pass


    # Enter a parse tree produced by calcParser#AddSub.
    def enterAddSub(self, ctx:calcParser.AddSubContext):
        pass

    # Exit a parse tree produced by calcParser#AddSub.
    def exitAddSub(self, ctx:calcParser.AddSubContext):
        pass


    # Enter a parse tree produced by calcParser#ParS.
    def enterParS(self, ctx:calcParser.ParSContext):
        pass

    # Exit a parse tree produced by calcParser#ParS.
    def exitParS(self, ctx:calcParser.ParSContext):
        pass


    # Enter a parse tree produced by calcParser#USign.
    def enterUSign(self, ctx:calcParser.USignContext):
        pass

    # Exit a parse tree produced by calcParser#USign.
    def exitUSign(self, ctx:calcParser.USignContext):
        pass


    # Enter a parse tree produced by calcParser#Num.
    def enterNum(self, ctx:calcParser.NumContext):
        pass

    # Exit a parse tree produced by calcParser#Num.
    def exitNum(self, ctx:calcParser.NumContext):
        pass


    # Enter a parse tree produced by calcParser#Pow.
    def enterPow(self, ctx:calcParser.PowContext):
        pass

    # Exit a parse tree produced by calcParser#Pow.
    def exitPow(self, ctx:calcParser.PowContext):
        pass


    # Enter a parse tree produced by calcParser#DivMul.
    def enterDivMul(self, ctx:calcParser.DivMulContext):
        pass

    # Exit a parse tree produced by calcParser#DivMul.
    def exitDivMul(self, ctx:calcParser.DivMulContext):
        pass


