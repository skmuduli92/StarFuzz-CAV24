@starfuzz: division_definition_lemma_1 []
@starfuzz: div [FStar.Math.Lib]

val division_definition_lemma_1: a:int -> b:pos -> m:int{(minus a b) < m * b} ->  Lemma (m > (div a (minus b 1)))
