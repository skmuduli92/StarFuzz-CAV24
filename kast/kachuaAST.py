#!/usr/bin/python3

class AST(object):
    pass


class FstarSig(AST):
    def __init__(self, name, paramlist):
        self.name = name
        self.params = paramlist

    def __str__(self):
        return ("function signature of:", self.name)
   

class Lemma(AST):
    def __init__(self, lemma):
        self.lemma = lemma

    def __str__(self):
        return self.lemma.__str__()

class Expression(AST):
    pass

# --Arithmetic Expressions--------------------------------------------

class ArithExpr(Expression):
    pass


class FunctionCall(Expression):
    def __init__(self, fname, arglist, typemap):
        self.name = fname
        self.args = arglist
        self.typemap = typemap

    def __str__(self):
        # building calling expression
        arg_str = []
        if self.name == 'FStar_String.length':
            return "(Z.to_int (" + self.name + " " + ' '.join([str(arg) for arg in self.args]) + "))"
        elif self.name == 'FStar_String.make':
            return "(" + self.name + " " + ' '.join([str(arg) for arg in self.args]) + ")"
        elif self.name == 'FStar_String.string_of_list' or self.name == 'FStar_String.list_of_string':
            return "(" + self.name + " " + ' '.join([str(arg) for arg in self.args]) + ")"
        elif self.name == 'FStar_String.sub':
          return "(" + self.name + " " + self.args[0] + ' ' + ' '.join([str(arg) for arg in self.args[1:]]) + ")"              
        elif self.name == 'FStar_Char.char_of_u32':
            return "(FStar_Char.char_of_u32 " + ' '.join([str(arg) for arg in self.args]) + ")"
        elif self.name == 'FStar_Char.u32_of_char':
            return "(FStar_Char.u32_of_char " + ' '.join([str(arg) for arg in self.args]) + ")"        
        elif self.name == 'U32.uint_to_t':
            return "(U32.uint_to_t " + ' '.join(['(Z.of_int ' + str(arg) + ')' for arg in self.args]) + ")"
        elif self.name == 'FStar_String.string_of_int':
            return "(FStar_String.string_of_int " + ' '.join(['( ' + str(arg) + ')' for arg in self.args]) + ")"
        elif self.name == 'FStar_String.string_charlist_int':
            return "(FStar_String.string_charlist_int " + ' '.join(['( ' + str(arg) + ')' for arg in self.args]) + ")"
        else:                
            return "(Z.to_int (" + self.name + " " + ' '.join(['(Z.of_int ' + str(arg) + ')' for arg in self.args]) + "))"         

class BinArithOp(ArithExpr):
    def __init__(self, expr1, expr2, opsymbol):
        self.lexpr = expr1
        self.rexpr = expr2
        self.symbol = opsymbol

    def __str__(self):
        return "(" + self.lexpr.__str__() + " " + self.symbol + " " + self.rexpr.__str__() + ")"


class UnaryArithOp(ArithExpr):
    def __init__(self, expr1, opsymbol):
        self.expr = expr1
        self.symbol = opsymbol

    def __str__(self):
        return '(' + self.symbol + self.expr.__str__() + ')'


class UMinus(UnaryArithOp):
    def __init__(self, lexpr):
        super().__init__(lexpr, "-")

    def __str__(self):
        return '(0 ' + self.symbol + ' ' + self.expr.__str__() + ')'        


class Sum(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "+")


class Diff(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "-")


class Mult(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "*")

class Div(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "/")

class Mod(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "mod")        

class StrCat(BinArithOp):
    def __init__(self, lexpr, rexpr):
        super().__init__(lexpr, rexpr, "^")

    def __str__(self):
        return "(FStar_String.strcat " + self.lexpr.__str__() + " " + self.rexpr.__str__() + ")"

# --Boolean Expressions-----------------------------------------------    
    
class BoolExpr(Expression):
    pass


class BinCondOp(BoolExpr):
    def __init__(self, expr1, expr2, opsymbol):
        self.lexpr = expr1
        self.rexpr = expr2
        self.symbol = opsymbol

    def __str__(self):
        return "(" + self.lexpr.__str__() + ' ' + self.symbol + ' ' + self.rexpr.__str__() + ")"


class AND(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "&&")

class OR(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "||")


class IMPLIES(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "==>")     

class LT(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "<")


class GT(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, ">")


class LTE(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "<=")


class GTE(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, ">=")


class EQ(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "=")


class NEQ(BinCondOp):
    def __init__(self, expr1, expr2):
        super().__init__(expr1, expr2, "<>")


class NOT(BoolExpr):
    def __init__(self, uexpr):
        self.expr = uexpr
        self.symbol = "not"

    def __str__(self):
        return "(" + self.symbol + self.expr.__str__() + ")"


class BoolTrue(BoolExpr):
    def __init__(self):
        pass

    def __str__(self):
        return "True"


class BoolFalse(BoolExpr):
    def __init__(self):
        pass

    def __str__(self):
        return "False"


class Value(Expression):
    pass


class Num(Value):
    def __init__(self, v):
        self.val = int(v)

    def __str__(self):
        return str(self.val)
    
class Hex(Value):
    def __init__(self, v):
        self.val = int(v, 16)

    def __str__(self):
        return str(self.val)


class Var(Value):
    def __init__(self, vname):
        self.varname = vname

    def __str__(self):
        return self.varname
