@starfuzz: div [FStar.Math.Lib]
val div: a:int -> b:pos -> Tot (c:int{(a < 0 ==> c < 0) /\ (a >= 0 ==> c >= 0)})
