@starfuzz: distributivity_sub_right []
@starfuzz: op_Multiply [FStar.Math.Lib]

val distributivity_sub_right: a:int -> b:int -> c:int -> Lemma ((op_Multiply a (minus b c)) = (op_Multiply a b) - (op_Multiply a c))
