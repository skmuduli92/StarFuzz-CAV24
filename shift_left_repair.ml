(* OCAML header *)
open FStar_Math_Lib
open FStar_String
open FStar_Char
open Batteries
open Batteries.IO
open Crowbar


(* OCAML target *)
let target v i =
	let retval = Z.shift_left (Z.of_int v) i in
	(* let res2 =  Prims.pow2 (Z.of_int i) in *)
	let res = (Z.shift_right retval i) in 
	Printf.printf "%s =? %s\n ()\n" (Z.to_string res) (Z.to_string retval) ;
	()
		(* failwith "oops crash!!" *)

let () = target 0 549755813888



(* OCAML header *)
open FStar_Math_Lib



(* 
let z_sl v i = 
	let retval = Z.shift_left (Z.of_int v) i in
	Printf.printf "%s\n" (Z.to_string retval)

let ml_sl v i =
	let retval = Z.mul (Z.of_int v) (Z.shift_left Z.one i) in
	Printf.printf "%s\n" (Z.to_string retval)


let () = 
	z_sl 0 549755813888;
	ml_sl 0 549755813888
 *)

(* let() = 
	Printf.printf "%s\n" (Z.to_string (Z.shift_left (Z.of_int 0) 549755813888)) *)