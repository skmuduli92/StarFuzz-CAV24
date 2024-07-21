@starfuzz: pow2_lt_compat []
@starfuzz: pow2 [FStar.Math.Lib]

val pow2_lt_compat: n:nat -> m:nat -> Lemma (requires (m < n)) (ensures  ((pow2 m) < (pow2 n)))
