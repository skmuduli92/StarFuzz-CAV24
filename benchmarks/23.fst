@starfuzz: make [FStar_String]
@starfuzz: string [FStar.String]

val make: l:nat -> x:char -> Tot (s:string {(length s) = l})
