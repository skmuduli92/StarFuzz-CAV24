@starfuzz: slash_star_axiom []
@starfuzz: div [FStar.Math.Lib]
@starfuzz: op_Multiply [FStar.Math.Lib]

val slash_star_axiom: a:nat -> b:pos -> c:nat -> Lemma (requires ((op_Multiply a b) = c)) (ensures  (a = (div c b)))