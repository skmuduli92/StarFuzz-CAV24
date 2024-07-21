@starfuzz: division_propriety []
@starfuzz: div [FStar.Math.Lib]

val division_propriety: a:int -> b:pos -> Lemma ((minus a b) < (div a b) * b /\ (div a b) * b <= a)
