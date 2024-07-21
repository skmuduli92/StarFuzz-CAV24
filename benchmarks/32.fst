@starfuzz: distributivity_add_right []
@starfuzz: op_Multiply [FStar.Math.Lib]

val distributivity_add_right: a:int -> b:int -> c:int -> Lemma (( op_Multiply a  (b + c)) = (op_Multiply a  b) + (op_Multiply a  c))
