

@starfuzz: op_Plus_Percent [FStar.Math.Lib]

val op_Plus_Percent : a:int -> p:pos -> Tot (res:int{ (a >= 0 ==> res = a % p) /\ (a < 0 ==> res = -((-a) % p)) }) 
