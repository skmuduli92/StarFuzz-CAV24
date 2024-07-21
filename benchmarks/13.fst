@starfuzz: abs_mul_lemma []
@starfuzz: abs [FStar.Math.Lib]
@starfuzz: op_Multiply [FStar.Math.Lib]


val abs_mul_lemma: a:int -> b:int -> Lemma ((abs (op_Multiply a  b)) = (op_Multiply (abs a) (abs b)))