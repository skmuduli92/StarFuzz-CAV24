@starfuzz: bounded_multiple_is_zero []
@starfuzz: op_Multiply [FStar.Math.Lib]

val bounded_multiple_is_zero: (x:int) -> (n:pos) -> Lemma  (requires (-n < (op_Multiply x n) /\ ((op_Multiply x n) < n))) (ensures( x = 0))
