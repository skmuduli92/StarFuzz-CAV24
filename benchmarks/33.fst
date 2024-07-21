@starfuzz: pow2_double_sum []
@starfuzz: pow2 [FStar.Math.Lib]
val pow2_double_sum: n:nat -> Lemma ((pow2 n) + (pow2 n) = (pow2 (n + 1)))
