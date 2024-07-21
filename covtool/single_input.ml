(* example.ml *)


open Batteries
open Batteries.IO
open Crowbar


let () =
Crowbar.(add_test ~name:"single_int_template" [int] (fun num -> 
  Printf.printf "output<%d>\n" num;
 ))


