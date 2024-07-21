@starfuzz: swap_mul []
@starfuzz: op_Multiply [FStar.Math.Lib]
val swap_mul: a:int -> b:int -> Lemma ((op_Multiply a  b) = (op_Multiply b a))
