@starfuzz: multiple_division_lemma []
@starfuzz: op_Multiply [FStar.Math.Lib]

val multiple_division_lemma: (a:int)-> (n:int {n > 0 \/ n < 0}) -> Lemma ((div (op_Multiply a n) n) = a)
