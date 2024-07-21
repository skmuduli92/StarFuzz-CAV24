(*
  This is a test case for the following specification:
  
  val op_Plus_Percent : (a:int) -> (p:pos) -> (res:int{ (a >= 0 ==> res == a % p) /\ (a < 0 ==> res == -((-a) % p)) }) 

  Link: https://github.com/FStarLang/FStar/blob/7f37fa99504413661c887cc23c6eb6706a18887e/ulib/FStar.Math.Lib.fst#L111  
*)


open FStar_Math_Lib
open Crowbar



let target a p =
	let retval = FStar_Math_Lib.op_Plus_Percent (Z.of_int a) (Z.of_int p) in
	let res = Z.to_int retval in
	if not ((((not(a >= 0)) || (res == (a mod p))) && ((not(a < 0)) || (res == (-((-a) mod p)))))) then
		failwith "oops crash!!"

let () = target (-4611686018427387904) 966350864406
    



