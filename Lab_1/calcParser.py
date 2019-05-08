# Generated from calc.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("(\4\2\t\2\4\3\t\3\3\2\7\2\b\n\2\f\2\16\2\13\13\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\30\n\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3#\n\3\f\3\16\3&\13")
        buf.write("\3\3\3\2\3\4\4\2\4\2\4\3\2\6\7\3\2\4\5\2,\2\t\3\2\2\2")
        buf.write("\4\27\3\2\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\13\3\2\2\2\t\7")
        buf.write("\3\2\2\2\t\n\3\2\2\2\n\f\3\2\2\2\13\t\3\2\2\2\f\r\7\2")
        buf.write("\2\3\r\3\3\2\2\2\16\17\b\3\1\2\17\20\7\13\2\2\20\21\5")
        buf.write("\4\3\2\21\22\7\f\2\2\22\30\3\2\2\2\23\24\t\2\2\2\24\30")
        buf.write("\5\4\3\5\25\30\7\n\2\2\26\30\7\b\2\2\27\16\3\2\2\2\27")
        buf.write("\23\3\2\2\2\27\25\3\2\2\2\27\26\3\2\2\2\30$\3\2\2\2\31")
        buf.write("\32\f\b\2\2\32\33\t\3\2\2\33#\5\4\3\t\34\35\f\7\2\2\35")
        buf.write("\36\t\2\2\2\36#\5\4\3\b\37 \f\t\2\2 !\7\3\2\2!#\5\4\3")
        buf.write("\2\"\31\3\2\2\2\"\34\3\2\2\2\"\37\3\2\2\2#&\3\2\2\2$\"")
        buf.write("\3\2\2\2$%\3\2\2\2%\5\3\2\2\2&$\3\2\2\2\6\t\27\"$")
        return buf.getvalue()


class calcParser ( Parser ):

    grammarFileName = "calc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'*'", "'/'", "'+'", "'-'", "<INVALID>", 
                     "','", "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "POW", "MUL", "DIV", "ADD", "SUB", "NUMBER", 
                      "COMA", "DECIMAL", "LPAR", "RPAR", "WS" ]

    RULE_prog = 0
    RULE_expr = 1

    ruleNames =  [ "prog", "expr" ]

    EOF = Token.EOF
    POW=1
    MUL=2
    DIV=3
    ADD=4
    SUB=5
    NUMBER=6
    COMA=7
    DECIMAL=8
    LPAR=9
    RPAR=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(calcParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calcParser.ExprContext)
            else:
                return self.getTypedRuleContext(calcParser.ExprContext,i)


        def getRuleIndex(self):
            return calcParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = calcParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << calcParser.ADD) | (1 << calcParser.SUB) | (1 << calcParser.NUMBER) | (1 << calcParser.DECIMAL) | (1 << calcParser.LPAR))) != 0):
                self.state = 4
                self.expr(0)
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(calcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return calcParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DecContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL(self):
            return self.getToken(calcParser.DECIMAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDec" ):
                listener.enterDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDec" ):
                listener.exitDec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec" ):
                return visitor.visitDec(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calcParser.ExprContext)
            else:
                return self.getTypedRuleContext(calcParser.ExprContext,i)

        def ADD(self):
            return self.getToken(calcParser.ADD, 0)
        def SUB(self):
            return self.getToken(calcParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ParSContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(calcParser.LPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(calcParser.ExprContext,0)

        def RPAR(self):
            return self.getToken(calcParser.RPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParS" ):
                listener.enterParS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParS" ):
                listener.exitParS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParS" ):
                return visitor.visitParS(self)
            else:
                return visitor.visitChildren(self)


    class USignContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.sign = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(calcParser.ExprContext,0)

        def SUB(self):
            return self.getToken(calcParser.SUB, 0)
        def ADD(self):
            return self.getToken(calcParser.ADD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUSign" ):
                listener.enterUSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUSign" ):
                listener.exitUSign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUSign" ):
                return visitor.visitUSign(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(calcParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class PowContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calcParser.ExprContext)
            else:
                return self.getTypedRuleContext(calcParser.ExprContext,i)

        def POW(self):
            return self.getToken(calcParser.POW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPow" ):
                listener.enterPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPow" ):
                listener.exitPow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPow" ):
                return visitor.visitPow(self)
            else:
                return visitor.visitChildren(self)


    class DivMulContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calcParser.ExprContext)
            else:
                return self.getTypedRuleContext(calcParser.ExprContext,i)

        def DIV(self):
            return self.getToken(calcParser.DIV, 0)
        def MUL(self):
            return self.getToken(calcParser.MUL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivMul" ):
                listener.enterDivMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivMul" ):
                listener.exitDivMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivMul" ):
                return visitor.visitDivMul(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = calcParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [calcParser.LPAR]:
                localctx = calcParser.ParSContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 13
                self.match(calcParser.LPAR)
                self.state = 14
                self.expr(0)
                self.state = 15
                self.match(calcParser.RPAR)
                pass
            elif token in [calcParser.ADD, calcParser.SUB]:
                localctx = calcParser.USignContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                localctx.sign = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==calcParser.ADD or _la==calcParser.SUB):
                    localctx.sign = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 18
                self.expr(3)
                pass
            elif token in [calcParser.DECIMAL]:
                localctx = calcParser.DecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 19
                self.match(calcParser.DECIMAL)
                pass
            elif token in [calcParser.NUMBER]:
                localctx = calcParser.NumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.match(calcParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 32
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = calcParser.DivMulContext(self, calcParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 23
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 24
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==calcParser.MUL or _la==calcParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 25
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = calcParser.AddSubContext(self, calcParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 26
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 27
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==calcParser.ADD or _la==calcParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 28
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = calcParser.PowContext(self, calcParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")

                        self.state = 30
                        localctx.op = self.match(calcParser.POW)
                        self.state = 31
                        localctx.right = self.expr(0)
                        pass

             
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         




