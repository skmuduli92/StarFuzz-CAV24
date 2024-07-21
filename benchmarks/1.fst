@starfuzz: abs [FStar.Math.Lib]
val abs: x:int -> Tot (y:int{ ((x >= 0) ==> ( y = x)) /\ ((x < 0) ==> y = -x) })
