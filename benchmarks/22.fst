@starfuzz: string_of_list_of_string [FStar.String]
@starfuzz: string_of_list [FStar.String]
@starfuzz: list_of_string [FStar.String]




val string_of_list_of_string: (s:string) -> Lemma ((string_of_list (list_of_string s)) = s)
