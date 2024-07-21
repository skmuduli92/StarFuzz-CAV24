@starfuzz: division_definition []
@starfuzz: div [FStar.Math.Lib]

val division_definition: a:int -> b:pos -> m:int{(minus a b) < (m * b) /\ (m * b) <= a} -> Lemma (m = (div a b))
