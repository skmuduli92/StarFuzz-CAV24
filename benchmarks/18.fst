@starfuzz: powx_lemma2 []
@starfuzz: powx [FStar.Math.Lib]

val powx_lemma2: x:int -> n:nat -> m:nat -> Lemma ((powx x n) * (powx x m) = (powx x (n + m)))