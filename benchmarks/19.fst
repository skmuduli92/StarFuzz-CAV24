
@starfuzz: string_of_int [FStar_String]
@starfuzz: string_charlist_int [FStar_String]


val string_of_int: (i: nat{i < (pow2 21)}) -> Tot (j: string {(string_charlist_int i) = j})



let rec load_string l buf =
	if l = 0ul then "" else
	//16-09-20 we miss String.init, proper refinements, etc
	let b = UInt8.v (Buffer.index buf 0ul) in
	let s = String.make 1 (Char.char_of_int b) in
	let t = load_string (l -^ 1ul) (Buffer.sub buf 1ul (l -^ 1ul)) in
	String.strcat s t