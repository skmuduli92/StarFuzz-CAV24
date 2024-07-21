@starfuzz: sub [FStar.String]
@starfuzz: string [FStar.String]

val sub: s:string -> i:nat -> l:nat{i + l <= (length s)} -> Tot (r: string {(length r) = l})
