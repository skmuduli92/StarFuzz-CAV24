@starfuzz: distributivity_add_left []
@starfuzz: op_Multiply [FStar.Math.Lib]

val distributivity_add_left: a:int -> b:int -> c:int -> Lemma (( op_Multiply (a + b) c) = (op_Multiply a c) + (op_Multiply b c))
