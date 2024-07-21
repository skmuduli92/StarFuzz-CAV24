@starfuzz: division_definition_lemma_2 []
@starfuzz: op_Multiply [FStar.Math.Lib]
@starfuzz: div [FStar.Math.Lib]

val division_definition_lemma_2: a:int -> b:pos -> (m:int{(op_Multiply m  b) <= a}) -> Lemma (m < (div a b) + 1)
