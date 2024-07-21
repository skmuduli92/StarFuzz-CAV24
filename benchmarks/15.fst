@starfuzz: div_non_eucl_decr_lemma []
@starfuzz: div [FStar.Math.Lib]
@starfuzz: abs [FStar.Math.Lib]

val div_non_eucl_decr_lemma: a:int -> b:pos -> Lemma ((abs (div_non_eucl a b)) <= (abs a))

