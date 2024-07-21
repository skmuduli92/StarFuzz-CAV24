(* OCAML header *)
open FStar_Math_Lib
open FStar_String
open FStar_Char
open Batteries
open Batteries.IO
open Crowbar



(* OCAML target *)
let target i =
	if not  ((FStar_String.string_of_int i) = (FStar_String.string_charlist_int i)) then
	Printf.printf "char_of_int %d \n" i

let () =
    Crowbar.(add_test ~name:"fuzz_char_of_int" [int]
	(fun i ->
		guard (i >= 0);
		guard (i < (Z.to_int (Prims.pow2 (Z.of_int 21))));
		target i
	))






