@starfuzz: max [FStar.Math.Lib]
val max: x:int -> y:int -> Tot (z:int{ (x >= y ==> z = x) /\ (x < y ==> z = y) })
