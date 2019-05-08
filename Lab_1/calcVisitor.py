# Generated from calc.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .calcParser import calcParser
else:
    from calcParser import calcParser

# This class defines a complete generic visitor for a parse tree produced by calcParser.

class calcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calcParser#prog.
    def visitProg(self, ctx:calcParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#Dec.
    def visitDec(self, ctx:calcParser.DecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#AddSub.
    def visitAddSub(self, ctx:calcParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#ParS.
    def visitParS(self, ctx:calcParser.ParSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#USign.
    def visitUSign(self, ctx:calcParser.USignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#Num.
    def visitNum(self, ctx:calcParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#Pow.
    def visitPow(self, ctx:calcParser.PowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#DivMul.
    def visitDivMul(self, ctx:calcParser.DivMulContext):
        return self.visitChildren(ctx)



del calcParser