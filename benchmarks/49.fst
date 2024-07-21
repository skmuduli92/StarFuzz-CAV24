@starfuzz: lemma_div_lt_nat []
@starfuzz: pow2 [FStar.Math.Lib]

val lemma_div_lt_nat: (a:int) -> (n:nat) -> (m:nat{m <= n}) -> Lemma (requires (a < (pow2 n))) (ensures  (a / (pow2 m) < (pow2 (minus n m))))
