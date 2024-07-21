@starfuzz: swap_neg_mul []
@starfuzz: op_Multiply [FStar.Math.Lib]

val swap_neg_mul: a:int -> b:int -> Lemma ((op_Multiply (-a)  b) = (op_Multiply a (-b)))
