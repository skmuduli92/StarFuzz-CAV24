@starfuzz: lemma_mult_lt_right []
@starfuzz: op_Multiply [FStar.Math.Lib]

val lemma_mult_lt_right: a:pos -> b:int -> c:int -> Lemma (requires (b < c)) (ensures  ((op_Multiply b a) < (op_Multiply c a)))
