(* 
	 INFO: crash is found, when fuzzing for the following spec 
	 val shift_left: (v:int) -> (i:nat) -> (res:int{res == v * (pow2 i)})

	 Link: https://github.com/FStarLang/FStar/blob/7f37fa99504413661c887cc23c6eb6706a18887e/ulib/FStar.Math.Lib.fst#L95
*)



open FStar_Math_Lib
open Crowbar

(* v: int, i: nat *)
let target v i =
	let retval = FStar_Math_Lib.shift_left (Z.of_int v) (Z.of_int i) in
	Printf.printf "shift_left %d %d = %s\n" v i (Z.to_string retval);
	()


let () = target 0 549755813888 (* crashing inputs *)


