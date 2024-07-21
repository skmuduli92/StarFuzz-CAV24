
import os
import sys
sys.path.insert(0, os.path.join("..", "parserlib"))

from parserlib.tlangParser import tlangParser
from parserlib.tlangVisitor import tlangVisitor

from kast import kachuaAST


class astGenPass(tlangVisitor):

    def __init__(self):
        self.repeatInstrCount = 0 # keeps count for no of 'repeat' instructions
        self.signame = None
        self.vars = [] # keeps track of variables declared and their types
                       # using list to keep track of the ordering of variables
        self.reflist = [] # keeps track of the refinement list
        self.lemma = None # keeps track of the lemma

    def visitStart(self, ctx:tlangParser.StartContext):
        reflist, lemma = self.visit(ctx.fstar_sig())
        self.reflist = reflist
        self.lemma = lemma
        return reflist, lemma

    def visitFstar_sig(self, ctx:tlangParser.Fstar_sigContext):
        # print('Visiting Fstar_sig:', ctx.NAME())
        # self.signame = ctx.NAME().getText()
        paramlist = self.visitParams(ctx.params())
        lemma = None
        if ctx.lemma():
            lemma = self.visitLemma(ctx.lemma())
            
        return paramlist, lemma

    def visitParams(self, ctx:tlangParser.ParamsContext):
        param_list = []
        for i in ctx.param():
            param_list.append(self.visit(i))

        return param_list

    # Visit a parse tree produced by tlangParser#param.
    def visitParam(self, ctx:tlangParser.ParamContext):
        tystr = self.visit(ctx.ty())
        name = ctx.NAME().getText()
        self.vars.append((name, tystr))

        if ctx.ty_refinement():
            return self.visit(ctx.ty_refinement())     

    # Visit a parse tree produced by tlangParser#ty_refinement.
    def visitTy_refinement(self, ctx:tlangParser.Ty_refinementContext):
        return self.visit(ctx.condition())

    # Visit a parse tree produced by tlangParser#ty.
    def visitTy(self, ctx:tlangParser.TyContext):
        return ctx.getText()
        
    #   Visit a parse tree produced by tlangParser#unaryExpr.
    def visitUnaryExpr(self, ctx:tlangParser.UnaryExprContext):
        expr1 = self.visit(ctx.expression())
        if ctx.unaryArithOp().MINUS():
            return kachuaAST.UMinus(expr1)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tlangParser#addExpr.
    def visitAddExpr(self, ctx:tlangParser.AddExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.additive().PLUS():
            return kachuaAST.Sum(left, right)
        elif ctx.additive().MINUS():
            return kachuaAST.Diff(left, right)


    # Visit a parse tree produced by tlangParser#mulExpr.
    def visitMulExpr(self, ctx:tlangParser.MulExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.multiplicative().MUL():
            return kachuaAST.Mult(left, right)
        elif ctx.multiplicative().DIV():
            return kachuaAST.Div(left, right)
        elif ctx.multiplicative().MOD():
            return kachuaAST.Mod(left, right)
        elif ctx.multiplicative().STRCAT():
            return kachuaAST.StrCat(left, right)

    def visitCondition(self, ctx:tlangParser.ConditionContext):
        if ctx.NOT():
            expr1 = self.visit(ctx.condition(0))        
            return kachuaAST.NOT(expr1)

        if ctx.logicOp():
            expr1 = self.visit(ctx.condition(0))
            expr2 = self.visit(ctx.condition(1))
            logicOpCtx = ctx.logicOp()

            if logicOpCtx.AND():
                return kachuaAST.AND(expr1, expr2)
            elif logicOpCtx.OR():
                return kachuaAST.OR(expr1, expr2)
            elif logicOpCtx.IMPLIES():
                return kachuaAST.OR(kachuaAST.NOT(expr1), expr2)
            
        
        if ctx.binCondOp():
            expr1 = self.visit(ctx.expression(0))
            expr2 = self.visit(ctx.expression(1))
            binOpCtx = ctx.binCondOp()

            if binOpCtx.LT():
                return kachuaAST.LT(expr1, expr2)
            elif binOpCtx.GT():
                return kachuaAST.GT(expr1, expr2)
            elif binOpCtx.EQ():
                return kachuaAST.EQ(expr1, expr2)
            elif binOpCtx.NEQ():
                return kachuaAST.NEQ(expr1, expr2)
            elif binOpCtx.LTE():
                return kachuaAST.LTE(expr1, expr2)
            elif binOpCtx.GTE():
                return kachuaAST.GTE(expr1, expr2)

        if ctx.condition():
            # condition is inside paranthesis
            return self.visit(ctx.condition(0))
            
        return self.visitChildren(ctx)

    def visitValue(self, ctx:tlangParser.ValueContext):
        if ctx.NUM():
            return kachuaAST.Num(ctx.NUM().getText())
        if ctx.HEX():
            return kachuaAST.Hex(ctx.HEX().getText())
        elif ctx.NAME():
            return kachuaAST.Var(ctx.NAME().getText())

    # Visit a parse tree produced by tlangParser#parenExpr.
    def visitParenExpr(self, ctx:tlangParser.ParenExprContext):
        return self.visit(ctx.pexpression())


    # Visit a parse tree produced by tlangParser#callExpr.
    def visitCallExpr(self, ctx:tlangParser.CallExprContext):
        exprList = [ self.visit(ctx.expression(i)) for i in range(len(ctx.expression()))]
        fname = ctx.fname().getText()

        if fname == "pow2":
            fname = "Prims.pow2"
        elif fname == "div":
            fname = "FStar_Math_Lib.div"
        elif fname == "powx":
            fname = "FStar_Math_Lib.powx"
        elif fname == "length":
            fname = "FStar_String.length"
        elif fname == "string_of_list":
            fname = "FStar_String.string_of_list"
        elif fname == "list_of_string":
            fname = "FStar_String.list_of_string"
        elif fname == "char_of_u32":
            fname = "FStar_Char.char_of_u32"
        elif fname == "u32_of_char":
            fname = "FStar_Char.u32_of_char"            
        elif fname == "make":
            fname = "FStar_String.make"
        elif fname == "pow2_buggy":
            fname = "Prims.pow2_buggy"
        elif fname == "abs":
            fname = "FStar_Math_Lib.abs"
        elif fname == "sub":
            fname = "FStar_String.sub"
        elif fname == "op_Multiply":
            fname = "Prims.op_Multiply"
        elif fname == "U32.uint_to_t":
            fname = "U32.uint_to_t"
        elif fname == "string_of_int":
            fname = "FStar_String.string_of_int"
        elif fname == "string_charlist_int":
            fname = "FStar_String.string_charlist_int"
        elif fname == "minus":
            if len(exprList) == 2:
                return kachuaAST.Diff(exprList[0], exprList[1])
            else: 
                raise ValueError("Invalid condition")
            
        else: fname = "FStar_Math_Lib." + fname

        print("Visiting CallExpr:", fname, self.vars)
        return kachuaAST.FunctionCall(fname, exprList, self.vars)
 

    # Visit a parse tree produced by tlangParser#exprPExpr.
    def visitExprPExpr(self, ctx:tlangParser.ExprPExprContext):
        return self.visit(ctx.expression())
    

    # Visit a parse tree produced by tlangParser#lemma.
    def visitLemma(self, ctx:tlangParser.LemmaContext):
        print('Visiting Lemma:', ctx.getText())
        require = self.visit(ctx.condition(0))
        if ctx.condition(1): 
            ensure = self.visit(ctx.condition(1))
            return kachuaAST.Lemma(kachuaAST.OR(kachuaAST.NOT(require), ensure))
        else:
            return kachuaAST.Lemma(require)