@starfuzz: lemma_div_def []
@starfuzz: div [FStar.Math.Lib]

val lemma_div_def: a:nat -> b:pos -> Lemma (a = b * (div a b) + a % b)