@starfuzz: pow2_plus []
@starfuzz: pow2 [FStar.Math.Lib]

val pow2_plus: n:nat -> m:nat -> Lemma (((pow2 n) * (pow2 m) = (pow2 (n + m))))
