@starfuzz: lemma_mult_le_left []
@starfuzz: op_Multiply [FStar.Math.Lib]

val lemma_mult_le_left: a:nat -> b:int -> c:int -> Lemma (requires (b <= c)) (ensures  ((op_Multiply a  b) <= (op_Multiply a c)))
