@starfuzz: min [FStar.Math.Lib]

val min: x:int -> y:int -> Tot (z:int{ (x >= y ==> z = y) /\ (x < y ==> z = x) })