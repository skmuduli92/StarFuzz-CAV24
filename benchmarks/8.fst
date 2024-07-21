

@starfuzz: signed_modulo [FStar.Math.Lib]

val signed_modulo: v:int -> p:pos -> Tot (res:int{ res = v - ((div_non_eucl v p) * p) })
