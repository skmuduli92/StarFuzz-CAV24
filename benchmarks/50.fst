@starfuzz: lemma_div_lt []
@starfuzz: pow2 [FStar.Math.Lib]

val lemma_div_lt: (a:int) -> (n:nat) -> (m:nat) -> Lemma  (requires (m <= n /\ a < (pow2 n)))  (ensures (a / (pow2 m) < (pow2 (minus n m))))
