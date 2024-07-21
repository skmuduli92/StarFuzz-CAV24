
grammar tlang;

start : fstar_sig EOF
      ;

fstar_sig : params ('->' lemma)?
        ;

params : param ('->' param )*
       ;

lemma : 
      'Lemma' '(' condition ')'
      | 'Lemma' '(' 'requires' condition ')' '(' 'ensures' condition ')';


// TODO: '{ expression }' could be optional, update it later '}'
param : 
      'Tot'? '(' NAME ':' ty ty_refinement? ')'
      | 'Tot'? NAME ':' ty ty_refinement?
      ;


ty_refinement : '{' condition '}'
            ;	      

condition : 
      NOT condition
      | '(' condition ')'
      | expression binCondOp expression
      | condition logicOp condition
      ;

ty : 'int' | 'pos' | 'nat' | 'string' | 'char' | 'char_code'
   ;

fname : 'length' | 'pow2' | 'div' | 'div_non_eucl' | 'abs' | 'signed_modulo' | 'powx'
      | 'char_of_u32' | 'U32.uint_to_t' | 'pow2_buggy' | 'op_Multiply' | 'string_of_list'
      | 'list_of_string' | 'make' | 'minus' | 'u32_of_char' | 'string_of_int' | 'string_charlist_int' 
      ;

expression : 
            unaryArithOp expression                 #unaryExpr
            | expression multiplicative expression  #mulExpr
            | expression additive expression        #addExpr
            | value                                 #valueExpr
            | '(' pexpression ')'                   #parenExpr
            ;

pexpression : 
            fname (expression)+                 #callExpr 
            | expression                        #exprPExpr
            ;


multiplicative : MUL | DIV | MOD | STRCAT;
additive : PLUS | MINUS;


unaryArithOp : MINUS ;

PLUS     : '+' ;
MINUS    : '-' ;
MUL      : '*' ;
DIV      : '/' ;
MOD      : '%' ;
STRCAT   : '^' ;


binCondOp :  EQ | NEQ | LT | GT | LTE | GTE
          ;

logicOp : 
            | NOT
            | AND 
            | OR 
            | IMPLIES;

LT : '<' ;
GT : '>' ;
EQ : '=';
NEQ: '!=';
LTE: '<=';
GTE: '>=';
AND: '/\\';
OR : '\\/';
NOT: '!' ;
IMPLIES: '==>';

value : NUM
      | HEX
      | NAME
      ;

NUM  : [0-9]+        ;
HEX  : '0x' [0-9a-fA-F]+
     ;

NAME : [a-zA-Z_] [a-zA-Z0-9_]*     ;

Whitespace: [ \t\n\r]+ -> skip;
