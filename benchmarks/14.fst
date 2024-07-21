@starfuzz: signed_modulo_property []
@starfuzz: abs [FStar.Math.Lib]
@starfuzz: signed_modulo [FStar.Math.Lib]

val signed_modulo_property: v:int -> p:pos -> Lemma ((abs (signed_modulo v p )) < p)
