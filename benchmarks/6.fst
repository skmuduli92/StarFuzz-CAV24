

@starfuzz: shift_left [FStar.Math.Lib]

val shift_left: v:int -> i:nat -> Tot (res:int{res = v * (pow2 i)})
