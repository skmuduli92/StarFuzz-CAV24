# Generated from tlang.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tlangParser import tlangParser
else:
    from tlangParser import tlangParser

# This class defines a complete listener for a parse tree produced by tlangParser.
class tlangListener(ParseTreeListener):

    # Enter a parse tree produced by tlangParser#start.
    def enterStart(self, ctx:tlangParser.StartContext):
        pass

    # Exit a parse tree produced by tlangParser#start.
    def exitStart(self, ctx:tlangParser.StartContext):
        pass


    # Enter a parse tree produced by tlangParser#fstar_sig.
    def enterFstar_sig(self, ctx:tlangParser.Fstar_sigContext):
        pass

    # Exit a parse tree produced by tlangParser#fstar_sig.
    def exitFstar_sig(self, ctx:tlangParser.Fstar_sigContext):
        pass


    # Enter a parse tree produced by tlangParser#params.
    def enterParams(self, ctx:tlangParser.ParamsContext):
        pass

    # Exit a parse tree produced by tlangParser#params.
    def exitParams(self, ctx:tlangParser.ParamsContext):
        pass


    # Enter a parse tree produced by tlangParser#param.
    def enterParam(self, ctx:tlangParser.ParamContext):
        pass

    # Exit a parse tree produced by tlangParser#param.
    def exitParam(self, ctx:tlangParser.ParamContext):
        pass


    # Enter a parse tree produced by tlangParser#ty_refinement.
    def enterTy_refinement(self, ctx:tlangParser.Ty_refinementContext):
        pass

    # Exit a parse tree produced by tlangParser#ty_refinement.
    def exitTy_refinement(self, ctx:tlangParser.Ty_refinementContext):
        pass


    # Enter a parse tree produced by tlangParser#condition.
    def enterCondition(self, ctx:tlangParser.ConditionContext):
        pass

    # Exit a parse tree produced by tlangParser#condition.
    def exitCondition(self, ctx:tlangParser.ConditionContext):
        pass


    # Enter a parse tree produced by tlangParser#ty.
    def enterTy(self, ctx:tlangParser.TyContext):
        pass

    # Exit a parse tree produced by tlangParser#ty.
    def exitTy(self, ctx:tlangParser.TyContext):
        pass


    # Enter a parse tree produced by tlangParser#expression.
    def enterExpression(self, ctx:tlangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by tlangParser#expression.
    def exitExpression(self, ctx:tlangParser.ExpressionContext):
        pass


    # Enter a parse tree produced by tlangParser#binArithOp.
    def enterBinArithOp(self, ctx:tlangParser.BinArithOpContext):
        pass

    # Exit a parse tree produced by tlangParser#binArithOp.
    def exitBinArithOp(self, ctx:tlangParser.BinArithOpContext):
        pass


    # Enter a parse tree produced by tlangParser#unaryArithOp.
    def enterUnaryArithOp(self, ctx:tlangParser.UnaryArithOpContext):
        pass

    # Exit a parse tree produced by tlangParser#unaryArithOp.
    def exitUnaryArithOp(self, ctx:tlangParser.UnaryArithOpContext):
        pass


    # Enter a parse tree produced by tlangParser#binCondOp.
    def enterBinCondOp(self, ctx:tlangParser.BinCondOpContext):
        pass

    # Exit a parse tree produced by tlangParser#binCondOp.
    def exitBinCondOp(self, ctx:tlangParser.BinCondOpContext):
        pass


    # Enter a parse tree produced by tlangParser#logicOp.
    def enterLogicOp(self, ctx:tlangParser.LogicOpContext):
        pass

    # Exit a parse tree produced by tlangParser#logicOp.
    def exitLogicOp(self, ctx:tlangParser.LogicOpContext):
        pass


    # Enter a parse tree produced by tlangParser#value.
    def enterValue(self, ctx:tlangParser.ValueContext):
        pass

    # Exit a parse tree produced by tlangParser#value.
    def exitValue(self, ctx:tlangParser.ValueContext):
        pass


