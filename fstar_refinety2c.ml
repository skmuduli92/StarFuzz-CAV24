(* Include the FStar_CheckedFiles module *)

open FStar_CheckedFiles
open FStar_Syntax_Syntax
open FStar_Ident
open FStar_Interactive_QueryHelper
open FStar_Syntax_Print

(* NOTE: you can print the type using the following function: tag_of_term <term> *)

(* let check_decl_typ t = term_to_string (FStar_Syntax_Util.canon_app t) *)

let binder_to_ppname b = FStar_Ident.string_of_id b.binder_bv.ppname
;;

let sort_to_csort s = match (term_to_string s) with
  | "Prims.int" -> "int"
  | _ -> term_to_string s (* TODO: add translation for more types *)
;;

let binder_to_string b =  match b.binder_bv.sort.n with
  | FStar_Syntax_Syntax.Tm_refine
      { FStar_Syntax_Syntax.b = xt; FStar_Syntax_Syntax.phi = f;_}
    -> (binder_to_ppname b) ^ " = (" ^ (sort_to_csort xt.sort) ^ " :: " ^ (term_to_string f) ^ ")"

  |_ -> failwith "Failed in binder_to_string function, expected FStar_Syntax_Syntax.Tm_refine"
;;

let check_binders bs =
  let check_binder b = (binder_to_string b) in
  List.map check_binder bs
;;

let binders_to_refinements bs=
  let binder_to_refn b = (
    match b.binder_bv.sort.n with
    | FStar_Syntax_Syntax.Tm_refine
        { FStar_Syntax_Syntax.b = xt; FStar_Syntax_Syntax.phi = f;_}
      ->    "  assume (" ^ (term_to_string f) ^ ");"
    |_ -> failwith "Failed in binder_to_refn function, expected FStar_Syntax_Syntax.Tm_refine"

  ) in

  String.concat "\n" (List.map binder_to_refn bs)
;;

let binder_to_cparam b = match b.binder_bv.sort.n with
  | FStar_Syntax_Syntax.Tm_refine
      { FStar_Syntax_Syntax.b = xt; FStar_Syntax_Syntax.phi = f;_}
    -> (sort_to_csort xt.sort) ^ " " ^ (binder_to_ppname b)

  |_ -> failwith "Failed in binder_to_string function, expected FStar_Syntax_Syntax.Tm_refine"
;;

let binders_to_csig bs =
  List.map binder_to_cparam bs
;;


let comp_to_retty c = match c.FStar_Syntax_Syntax.n with
  | FStar_Syntax_Syntax.Total t ->
    (
      let tm =  t.FStar_Syntax_Syntax.n in
      match tm with
      | FStar_Syntax_Syntax.Tm_refine
          { FStar_Syntax_Syntax.b = xt; FStar_Syntax_Syntax.phi = f;_}
        -> (sort_to_csort xt.sort)

      | _ -> failwith "Type other than Tm_refine is not recognized"
    )

  | _ -> failwith "Type other than Total is not recognized"
;;

let comp_to_ppanme c = match c.FStar_Syntax_Syntax.n with
  | FStar_Syntax_Syntax.Total t ->
    (
      let tm =  t.FStar_Syntax_Syntax.n in
      match tm with
      | FStar_Syntax_Syntax.Tm_refine
          { FStar_Syntax_Syntax.b = xt; FStar_Syntax_Syntax.phi = f;_}
        -> (FStar_Ident.string_of_id xt.ppname)

      | _ -> failwith "Type other than Tm_refine is not recognized"
    )

  | _ -> failwith "Type other than Total is not recognized"
;;

let check_decl_typ t =
  match t.FStar_Syntax_Syntax.n with
  | FStar_Syntax_Syntax.Tm_arrow
      { FStar_Syntax_Syntax.bs1 = bs;
        FStar_Syntax_Syntax.comp = c;_}
    ->
    let bstr = String.concat ", " (binders_to_csig bs) in
    let compstr = comp_to_string c in
    FStar_Compiler_Util.format2 "%s\n%s" bstr compstr

  | _ -> failwith "Failed in binder_to_string function, expected FStar_Syntax_Syntax.Tm_arrow"
;;

let comp_to_cparam c = match c.FStar_Syntax_Syntax.n with
  | FStar_Syntax_Syntax.Total t ->
    (
      let tm =  t.FStar_Syntax_Syntax.n in
      match tm with
      | FStar_Syntax_Syntax.Tm_refine
          { FStar_Syntax_Syntax.b = xt; FStar_Syntax_Syntax.phi = f;_}
        -> (sort_to_csort xt.sort) ^ " " ^ (FStar_Ident.string_of_id xt.ppname)

      | _ -> failwith "Type other than Tm_refine is not recognized"
    )

  | _ -> failwith "Type other than Total is not recognized"
;;

let get_call_str lid t =
  match t.FStar_Syntax_Syntax.n with
  | FStar_Syntax_Syntax.Tm_arrow
      { FStar_Syntax_Syntax.bs1 = bs;
        FStar_Syntax_Syntax.comp = c;_}
    ->

    let bstr = String.concat ", " (List.map binder_to_ppname bs) in
    let compstr = comp_to_ppanme c in
    let retty = comp_to_retty c in
    let fname = lid_to_string lid in
    FStar_Compiler_Util.format4 "  %s %s = %s(%s);" retty compstr fname bstr

  | _ -> failwith "Failed in binder_to_string function, expected FStar_Syntax_Syntax.Tm_arrow"
;;


let rec sig_to_string t =
  match t.FStar_Syntax_Syntax.n with
  | FStar_Syntax_Syntax.Tm_arrow
      { FStar_Syntax_Syntax.bs1 = bs;
        FStar_Syntax_Syntax.comp = c;_}
    -> String.concat ", " (binders_to_csig bs)
  | _ -> failwith "Failed in binder_to_string function, expected FStar_Syntax_Syntax.Tm_arrow"
;;

let rec sig_to_varlist t =
  match t.FStar_Syntax_Syntax.n with
  | FStar_Syntax_Syntax.Tm_arrow
      { FStar_Syntax_Syntax.bs1 = bs;
        FStar_Syntax_Syntax.comp = c;_}
    ->
    let bstr = String.concat ", " (List.map binder_to_ppname bs)
    and compstr = comp_to_cparam c in
    (FStar_Compiler_Util.format2 "%s, %s" bstr compstr)

  | _ -> failwith "Failed in binder_to_string function, expected FStar_Syntax_Syntax.Tm_arrow"
;;

let get_assumptions t =   match t.FStar_Syntax_Syntax.n with
  | FStar_Syntax_Syntax.Tm_arrow
      { FStar_Syntax_Syntax.bs1 = bs;
        FStar_Syntax_Syntax.comp = c;_}
    -> binders_to_refinements bs

  | _ -> failwith "Failed in binder_to_string function, expected FStar_Syntax_Syntax.Tm_arrow"
;;

let get_assert t =
  let comp_to_assert cm = (
    match cm.FStar_Syntax_Syntax.n with
    | FStar_Syntax_Syntax.Total t ->
      (
        let tm =  t.FStar_Syntax_Syntax.n in
        match tm with
        | FStar_Syntax_Syntax.Tm_refine
            { FStar_Syntax_Syntax.b = xt; FStar_Syntax_Syntax.phi = f;_}
          -> "  assert (" ^ term_to_string f ^ ");"

        | _ -> failwith "Type other than Tm_refine is not recognized"
      )

    | _ -> failwith "Type other than Total is not recognized"

  ) in
  match t.FStar_Syntax_Syntax.n with
  | FStar_Syntax_Syntax.Tm_arrow
      { FStar_Syntax_Syntax.bs1 = bs;
        FStar_Syntax_Syntax.comp = c;_}
    ->
    comp_to_assert c

  | _ -> failwith "Failed in binder_to_string function, expected FStar_Syntax_Syntax.Tm_arrow"
;;

let sigelt_to_string (s: FStar_Syntax_Syntax.sigelt) =
  match s.sigel with
  | FStar_Syntax_Syntax.Sig_declare_typ
      { FStar_Syntax_Syntax.lid2 = lid;
        FStar_Syntax_Syntax.us2 = univs; FStar_Syntax_Syntax.t2 = t; _ }
    ->
    let sigstr = sig_to_string t in
    (* let funname = lid_to_string lid in  *)
    let funsig = ("void spec_fuzz") ^ " (" ^ sigstr  ^ ")" in
    let assume_body = get_assumptions t in
    let assert_body = get_assert t in
    let call_str = get_call_str lid t in
    FStar_Compiler_Util.format4 "%s\n{\n%s\n\n%s\n%s\n}\n" funsig assume_body call_str assert_body

  | _ -> failwith "none"
;;

let sigelts_to_string (m: FStar_Syntax_Syntax.modul) =
  FStar_Compiler_List.map sigelt_to_string m.declarations

let mod_to_string (m : FStar_Syntax_Syntax.modul) : Prims.string =
    FStar_Compiler_Effect.op_Bar_Greater (sigelts_to_string m) (FStar_String.concat "\n")
;;

let check_tc_results tc_result = mod_to_string tc_result.checked_module
;;

let write_to_file filename content =
  let oc = open_out filename in
  output_string oc content;
  close_out oc;
;;

let () =
  try
    (* Check if an argument is provided in the command line *)
    if Array.length Sys.argv = 1 then
      failwith "Please provide the name of the FStar checked file as an argument."
      (* Get the filename provided as a command line argument *)
    else let checked_filename = Sys.argv.(1) in
      (* Call the unsafe_raw_load_checked_file function with the filename *)
      match unsafe_raw_load_checked_file checked_filename with
      | Some (_, _, tc_result) ->
        let fuzz_target = check_tc_results tc_result in
        write_to_file "spec_target.c" fuzz_target;
        Printf.printf("Parsing Done! Generated 'spec_target.c' file.\n")

      | _ ->
        failwith "Failed to load the checked file."
  with
  | Failure msg -> Printf.eprintf "Error: %s\n" msg
  | Sys_error msg -> Printf.eprintf "System error: %s\n" msg
  | ex -> Printf.eprintf "An unexpected error occurred: %s\n" (Printexc.to_string ex)
