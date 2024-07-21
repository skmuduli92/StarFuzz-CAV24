@starfuzz: lemma_cancel_mul []
@starfuzz: op_Multiply [FStar.Math.Lib]
val lemma_cancel_mul: (a:int) -> (b:int) -> (n : pos) -> Lemma (requires ((op_Multiply a n) = (op_Multiply b n))) (ensures (a = b))
