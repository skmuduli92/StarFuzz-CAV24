open Batteries
open Batteries.IO
open FStar_String
open FStar_Char

type char = FStar_Char.char

let rec pow2 n =
  if n = 0 then 1
  else 2 * pow2 (n - 1)
;;

let char_of_int_fuzz num : char = (FStar_Char.char_of_u32 (U32.uint_to_t num))
;;

let fixed_test_driver num =
  if (num >= 0 && num <= 0xd7ff) || (num >= 0xe000 && num <= 0x10ffff)  
  then
    let test = FStar_String.string_of_list [char_of_int_fuzz (Prims.of_int num)] in
    print_endline test;
;;


let buggy_test_driver num =
  (* Buggy refinement: old pre-condition will cause crash (num: nat{i < pow2 21})*)
  if (num >= 0 && num < (pow2 21))
  then
    let test = FStar_String.make Z.one (char_of_int_fuzz (Z.of_int num)) in
    Printf.printf "%s" test
;;


let () =
  Crowbar.(add_test ~name:"PR2550" [int] (fun num -> buggy_test_driver num))
