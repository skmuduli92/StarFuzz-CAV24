@starfuzz: small_div []
@starfuzz: div [FStar.Math.Lib]
val small_div: (a:nat) -> (n:pos) -> Lemma (requires (a < n)) (ensures ((div a n) = 0))
