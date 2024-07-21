@starfuzz: char_of_u32_of_char []
@starfuzz: char_of_u32 [FStar.Char]
@starfuzz: u32_of_char [FStar.Char]


val char_of_u32_of_char: (c: char) -> Lemma ((char_of_u32 (u32_of_char c)) = c)
