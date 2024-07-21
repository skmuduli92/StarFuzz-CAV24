@starfuzz: distributivity_sub_left []
@starfuzz: op_Multiply [FStar.Math.Lib]

val distributivity_sub_left: a:int -> b:int -> c:int -> Lemma ((op_Multiply (minus a b) c) = (op_Multiply a c) - (op_Multiply b c))
