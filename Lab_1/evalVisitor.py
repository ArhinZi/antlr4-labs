from calcVisitor import calcVisitor
from calcParser import calcParser

class evalVisitor(calcVisitor):

    # Visit a parse tree produced by calcParser#prog.
    def visitProg(self, ctx:calcParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#USigb.
    def visitUSign(self, ctx:calcParser.USignContext):
        if(ctx.SUB() is not None):
            # print(type(self.visitChildren(ctx).getText()))
            return (-1 * self.visitChildren(ctx))
        else:
            return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#Dec.
    def visitDec(self, ctx:calcParser.DecContext):
        return float(ctx.DECIMAL().getText())


    # Visit a parse tree produced by calcParser#AddSub.
    def visitAddSub(self, ctx:calcParser.AddSubContext):
        if(ctx.SUB() is not None):
            return self.visit(ctx.left) - self.visit(ctx.right)
        else:
            return self.visit(ctx.left) + self.visit(ctx.right)


    # Visit a parse tree produced by calcParser#ParS.
    def visitParS(self, ctx:calcParser.ParSContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by calcParser#Num.
    def visitNum(self, ctx:calcParser.NumContext):
        return int(ctx.NUMBER().getText())


    # Visit a parse tree produced by calcParser#Pow.
    def visitPow(self, ctx:calcParser.PowContext):
        return self.visit(ctx.left) ** self.visit(ctx.right)


    # Visit a parse tree produced by calcParser#DivMul.
    def visitDivMul(self, ctx:calcParser.DivMulContext):
        if (ctx.DIV() is not None):
            return self.visit(ctx.left) / self.visit(ctx.right)
        else:
            return self.visit(ctx.left) * self.visit(ctx.right)
