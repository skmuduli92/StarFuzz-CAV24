@starfuzz: pow2_minus []
@starfuzz: pow2 [FStar.Math.Lib]

val pow2_minus: (n:nat) -> (m:nat{ n >= m }) -> Lemma ((pow2 n) / (pow2 m) = (pow2 (minus n m)))
