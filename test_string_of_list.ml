
open Batteries
open Batteries.IO
open FStar_String
open FStar_Char

open Crowbar



let buggy_instance num =
  (* if ((num >= 0) && (num < (Z.to_int (Prims.pow2 (Z.of_int 21))))) then *)
    let s = FStar_String.string_of_list [FStar_Char.char_of_int (Prims.of_int num)] in
    let t = FStar_String.list_of_string s in
    let s' = FStar_String.string_of_list t in
    if s <> s' then
      failwith "buggy"


let () =
Crowbar.(add_test ~name:"PR2550" [int] (fun num -> 
  guard ((num >= 0 && num <= 0xd7ff) || (num >= 0xe000 && num <= 0x10ffff));
  (* guard ((num >= 0) && (num < (Z.to_int (Prims.pow2 (Z.of_int 21))))); *)
  buggy_instance num))
