@starfuzz: pow2_le_compat []
@starfuzz: pow2 [FStar.Math.Lib]

val pow2_le_compat: n:nat -> m:nat -> Lemma (requires (m <= n)) (ensures  ((pow2 m) <= (pow2 n)))
