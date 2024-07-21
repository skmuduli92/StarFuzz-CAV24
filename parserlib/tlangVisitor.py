# Generated from tlang.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tlangParser import tlangParser
else:
    from tlangParser import tlangParser

# This class defines a complete generic visitor for a parse tree produced by tlangParser.

class tlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tlangParser#start.
    def visitStart(self, ctx:tlangParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#fstar_sig.
    def visitFstar_sig(self, ctx:tlangParser.Fstar_sigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#params.
    def visitParams(self, ctx:tlangParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#lemma.
    def visitLemma(self, ctx:tlangParser.LemmaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#param.
    def visitParam(self, ctx:tlangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#ty_refinement.
    def visitTy_refinement(self, ctx:tlangParser.Ty_refinementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#condition.
    def visitCondition(self, ctx:tlangParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#ty.
    def visitTy(self, ctx:tlangParser.TyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#fname.
    def visitFname(self, ctx:tlangParser.FnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#unaryExpr.
    def visitUnaryExpr(self, ctx:tlangParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#valueExpr.
    def visitValueExpr(self, ctx:tlangParser.ValueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#addExpr.
    def visitAddExpr(self, ctx:tlangParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#mulExpr.
    def visitMulExpr(self, ctx:tlangParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#parenExpr.
    def visitParenExpr(self, ctx:tlangParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#callExpr.
    def visitCallExpr(self, ctx:tlangParser.CallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#exprPExpr.
    def visitExprPExpr(self, ctx:tlangParser.ExprPExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#multiplicative.
    def visitMultiplicative(self, ctx:tlangParser.MultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#additive.
    def visitAdditive(self, ctx:tlangParser.AdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#unaryArithOp.
    def visitUnaryArithOp(self, ctx:tlangParser.UnaryArithOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#binCondOp.
    def visitBinCondOp(self, ctx:tlangParser.BinCondOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#logicOp.
    def visitLogicOp(self, ctx:tlangParser.LogicOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#value.
    def visitValue(self, ctx:tlangParser.ValueContext):
        return self.visitChildren(ctx)



del tlangParser