@starfuzz: multiply_fractions []
@starfuzz: op_Multiply [FStar.Math.Lib]
@starfuzz: div [FStar.Math.Lib]

val multiply_fractions: (a:int) -> (n:int {(n > 0 \/ n < 0)}) -> Lemma ((op_Multiply n (div a n ) ) <= a)
