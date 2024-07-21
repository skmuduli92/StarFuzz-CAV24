open Batteries
open Batteries.IO
open FStar_String
open FStar_Char

type char = FStar_Char.char

let char_of_int_old num : char = (FStar_Char.char_of_u32 (U32.uint_to_t num))
;;

let buggy_test_driver num =
  (* Buggy refinement: old pre-condition will cause crash (num: nat{i < pow2 21})*)
  if (num >= 0 && num < (Z.to_int (Prims.pow2 (Z.of_int 21))) )
  then
    let test = FStar_String.make Z.one (char_of_int_old (Z.of_int num)) in
    Printf.printf "%s" test
;;


(* let () =
  Crowbar.(add_test ~name:"PR2550" [int] (fun num -> buggy_test_driver num)) *)

let () = buggy_test_driver 55297