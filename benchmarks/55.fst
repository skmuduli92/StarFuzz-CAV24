@starfuzz: lt_square_div_lt []
@starfuzz: div [FStar.Math.Lib]

val lt_square_div_lt: (a:nat) -> (b:pos) -> Lemma (requires (a < (op_Multiply b b))) (ensures ((div a b) < b))