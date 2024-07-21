@starfuzz: neg_mul_left []
@starfuzz: op_Multiply [FStar.Math.Lib]

val neg_mul_left: a:int -> b:int -> Lemma (-(op_Multiply a b) = (op_Multiply (-a) b))
