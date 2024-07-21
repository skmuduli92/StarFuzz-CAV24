@starfuzz: lemma_eucl_div_bound []
@starfuzz: op_Multiply [FStar.Math.Lib]

val lemma_eucl_div_bound: a:int -> b:int -> q:int -> Lemma (requires (a < q)) (ensures  (a + (op_Multiply q b) < (op_Multiply q (b+1) ) ) )
