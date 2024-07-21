val string_of_list_of_string: (s:string) -> Lemma ((string_of_list (list_of_string s)) = s)
val make: l:nat -> x:char -> Tot (s:string {(length s) = l})

val char_of_u32_of_char: (c: char) -> Lemma ((char_of_u32 (u32_of_char c)) = c)

// val u32_of_char_of_u32: (c: char_code) -> Lemma (((u32_of_char (char_of_u32 c)) = c))

