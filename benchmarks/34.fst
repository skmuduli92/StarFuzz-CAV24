@starfuzz: pow2_double_mult []
@starfuzz: pow2 [FStar.Math.Lib]

val pow2_double_mult: n:nat -> Lemma ((op_Multiply 2 (pow2 n)) = (pow2 (n + 1)))
