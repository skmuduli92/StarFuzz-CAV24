@starfuzz: div_non_eucl_bigger_denom_lemma []
@starfuzz: div_non_eucl [FStar.Math.Lib]

val div_non_eucl_bigger_denom_lemma: a:int -> b:pos -> Lemma (requires (b > (abs a))) (ensures  ((div_non_eucl a b) = 0))
