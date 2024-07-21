@starfuzz: lemma_mult_le_right []
val lemma_mult_le_right: a:nat -> b:int -> c:int -> Lemma (requires (b <= c)) (ensures  ((op_Multiply b a) <= (op_Multiply c a)))
