(* OCAML header *)
open FStar_Math_Lib
open Crowbar




(* OCAML target *)
let target a b =
	let ct = FStar_Math_Lib.div (Z.of_int a) (Z.of_int b) in
	let c = Z.to_int ct in
	if not ((((not(a < 0)) || (c < 0)) && ((not(a >= 0)) || (c >= 0)))) then
		failwith "oops crash!!"


let () =
    Crowbar.(add_test ~name:"fuzz_div" [int; int]
	(fun a b ->
		guard (b > 0);
		target a b
	))



