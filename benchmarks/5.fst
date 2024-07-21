

@starfuzz: div_non_eucl [FStar.Math.Lib]

val div_non_eucl: a:int -> b:pos -> Tot (q:int{ ( a >= 0 ==> q = a / b ) /\ ( a < 0 ==> q = -((-a)/b) ) })
