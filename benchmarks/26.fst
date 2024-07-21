@starfuzz: lemma_mult_lt_left []
@starfuzz: op_Multiply [FStar.Math.Lib]

val lemma_mult_lt_left: a:pos -> b:int -> c:int -> Lemma (requires (b < c)) (ensures  ((op_Multiply a b) < ((op_Multiply a c))))
