@starfuzz: nat_over_pos_is_nat []
@starfuzz: div [FStar.Math.Lib]

val nat_over_pos_is_nat: a:nat -> b:pos -> Lemma ((div a b) >= 0)
