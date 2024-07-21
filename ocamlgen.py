
import antlr4

from parserlib.parseError import *
from parserlib.tlangParser import tlangParser
from parserlib.tlangLexer import tlangLexer

from kast import kachuaAST

import io
import re

def pretty_print(ir):
    print('\n========== IR ==========')
    for idx, item in enumerate(ir):
        print(f'refinement-{idx}', item)
    print('========================\n')


def parse_function_name(input_string):
    # Define a regular expression pattern to match the function name
    pattern = re.compile(r'val\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*:\s*')

    # Search for the pattern in the input string
    match = pattern.search(input_string)

    # Check if a match is found
    if match:
        # Extract and return the function name
        return match.group(1)
    else:
        # Return None if no match is found
        return None
    
def get_strings_after_colon(input_string):
    # Define a regular expression pattern to match the string after the first colon
    pattern = re.compile(r':\s*(.*)')

    # Search for the pattern in the input string
    match = pattern.search(input_string)

    # Check if a match is found
    if match:
        # Extract and return the string after the first colon
        return match.group(1)
    else:
        # Return None if no match is found
        return None    

def getParseTree(input):
    print('parsing input: ', input)
    signame = parse_function_name(input)
    spec_body = get_strings_after_colon(input)

    if signame is None:
        raise SyntaxError('Syntax Error: Invalid specification file: missing function name')
    
    if spec_body is None:
        raise SyntaxError('Syntax Error: Invalid specification file: missing specification body')

    try:
        lexer = tlangLexer(antlr4.InputStream(spec_body))
        stream = antlr4.CommonTokenStream(lexer)
        lexer._listeners = [SyntaxErrorListener()]
        tparser = tlangParser(stream)
        tparser._listeners = [SyntaxErrorListener()]
        tree = tparser.start()
    except Exception as e:
        print('\033[91m\n====================')
        print(e.__str__() + '\033[0m\n')
        exit(1)

    return signame, tree


def ocaml_header(outfl):
    f = io.StringIO()

    # write to file
    f.write('(* OCAML header *)\n')
    f.write('open FStar_Math_Lib\n')
    f.write('open FStar_String\n')
    f.write('open FStar_Char\n')
    f.write('open Batteries\n')
    f.write('open Batteries.IO\n')
    f.write('open Crowbar\n')
    f.write('\n\n\n')

    return f.getvalue()

"""
let () =
  Crowbar.(add_test ~name:"identity function" [int; int]
             (fun x y ->
               # generate list of conditions of following format [(guard condition_i);]
               <guard conditions>
               target <[list of input vars]>))

"""        


def find_var_type(guard, varmap):
    for item in varmap:
        if item[0] in str(guard):
            return item[1]
    return None

def crowbar_signature(guards, astbuilder, outfl):
    varmap = astbuilder.vars
    if astbuilder.lemma is None: guards = guards[:-1]
    if astbuilder.lemma is None: varmap = astbuilder.vars[:-1]
    signame = astbuilder.signame

    f = io.StringIO()
    crowbar_signature_head = f"""
let () =
    Crowbar.(add_test ~name:"fuzz_{signame}" """  

    # write to file
    f.write(crowbar_signature_head)
    f.write('[')
    for idx, item in enumerate(varmap):
        val = item[1]
        if val == 'pos' or val == 'nat': val = 'int'
        elif val == 'string': val = 'bytes'
        elif val == 'char' : val = 'int'
        elif val == 'char_code' : val = 'int'
        
        if idx == len(varmap) - 1:
            f.write(f'{val}')
        else:
            f.write(f'{val}; ')
    f.write(']\n')

    f.write('\t(fun ')
    for idx, item in enumerate(varmap):
        if idx == len(varmap) - 1:
            f.write(f'{item[0]}')
        else:
            f.write(f'{item[0]} ')

    f.write(' ->\n')
    # write guards for crowbar

    for var in varmap:
        if var[1] == 'pos':
            f.write(f'\t\tguard ({var[0]} > 0);\n')
        elif var[1] == 'nat':
            f.write(f'\t\tguard ({var[0]} >= 0);\n')
        elif var[1] == 'char_code':
            f.write(f'\t\tguard ({var[0]} >= 0);\n') # n < 0xd7ff \/ (U32.v n >= 0xe000 /\ U32.v n <= 0x10ffff
            f.write(f'\t\tguard (({var[0]} <= 0x10ffff) || ({var[0]} >= 0xe000 && {var[0]} <= 0x10ffff));\n')
    for g in guards:
        if g is None:
            continue

        f.write('\t\t')
        f.write(f'(guard {str(g)});\n')
        
    f.write('\t\ttarget ')
    
    for idx, item in enumerate(varmap):
        if idx == len(varmap) - 1:
            f.write(f'{item[0]}')
        else:
            f.write(f'{item[0]} ')
    f.write('\n\t))\n')
    f.write('\n\n\n')

    return f.getvalue()


def ocaml_target_method(ir, astbuilder):
    varmap = astbuilder.vars
    if astbuilder.lemma is None: varmap = astbuilder.vars[:-1]

    f = io.StringIO()
    f.write('(* OCAML target *)\n')
    f.write('let target ')
    for idx, item in enumerate(varmap):
        if idx == len(varmap) - 1:
            f.write(f'{item[0]}')
        else:
            f.write(f'{item[0]} ')

    f.write(' =\n')
    if astbuilder.lemma is None:
        f.write('\tlet retval = ') 
        # TODO: take package name as input too while running the tool for the spec signature
        if (astbuilder.signame == 'sub'):
            f.write(f'FStar_String.{astbuilder.signame} ')
        elif (astbuilder.signame == 'make'):
            f.write(f'FStar_String.{astbuilder.signame} ')
        elif (astbuilder.signame == 'char_of_int'):
            f.write(f'FStar_Char.{astbuilder.signame} ')
        elif (astbuilder.signame == 'pow2_buggy'):
            f.write(f'Prims.{astbuilder.signame} ')
        # elif(astbuilder.signame == 'U32.uint_to_t'):
        #     f.write(f'{astbuilder.signame}')
        elif (astbuilder.signame == 'string_of_int'):
            f.write(f'FStar_String.{astbuilder.signame} ')
        else: 
            f.write(f'FStar_Math_Lib.{astbuilder.signame} ')

        if (astbuilder.signame == 'make'):
            # return "(" + self.name + " " + ' '.join([str(arg) for arg in self.args]) + ")"
            decl = f"(Z.of_int {varmap[0][0]}) {varmap[1][0]}"
            f.write(f'{decl}')
        elif (astbuilder.signame == 'string_of_int'):
            f.write(f'( {varmap[0][0]})')
        else:    
            for idx, item in enumerate(varmap):
                cast_str = "" if item[1] == 'string' else "Z.of_int"
                if idx == len(varmap) - 1:
                    f.write(f'({cast_str} {item[0]})')
                else:
                    f.write(f'({cast_str} {item[0]}) ')
        
        f.write(' in\n')
        
        if (astbuilder.signame == 'char_of_int'):
            f.write(f'\tlet {astbuilder.vars[-1][0]} = retval in\n')
        elif (astbuilder.signame == 'sub') or (astbuilder.signame == 'make') or (astbuilder.signame == 'string_of_int'):
            f.write(f'\tlet {astbuilder.vars[-1][0]} = retval in\n')
        else:
            f.write(f'\tlet {astbuilder.vars[-1][0]} = Z.to_int retval in\n')
   
    # for cond in ir[:-1]:
    #     if cond is None:
    #         continue
    #     f.write('\tif (')
    #     f.write(f'({cond})')
    #     f.write(') then\n')
    #     f.write('\t\tfailwith "oops crash!!"\n')

    f.write('\tif not (')

    # TODO: right now we have benchmarks with refinement on the last variable only
    #       but this needs to be generalized to all variables
     
    if ir[-1]: 
        f.write(f'({ir[-1]})')

    if ir[-1] and astbuilder.lemma:
        f.write(' && ')

    if astbuilder.lemma:
        f.write(f'({astbuilder.lemma})')

    if ir[-1] is None and astbuilder.lemma is None:
        f.write('false')

    f.write(') then\n')
    f.write('\t\tfailwith "oops crash!!"\n')

    return f.getvalue()


def dump_ocaml_target(ir, astbuilder, outfl):
    # print red text
    header = ocaml_header(outfl)
    cbsig = crowbar_signature(ir, astbuilder , outfl)
    target = ocaml_target_method(ir, astbuilder)

    with open(outfl, 'w') as f:
        f.write(header)
        f.write(target)
        f.write(cbsig)

    # print(header)
    # print(target)
    # print(cbsig)