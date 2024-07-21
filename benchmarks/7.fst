

@starfuzz: arithmetic_shift_right [FStar.Math.Lib]

val arithmetic_shift_right: v:int -> i:nat -> Tot (res:int{ res = (div v (pow2 i)) })
