

@starfuzz: concat_length []
@starfuzz: length [FStar.String]


val concat_length: s1:string -> s2: string -> Lemma ( (length (s1 ^ s2)) = (length s1) + (length s2))
