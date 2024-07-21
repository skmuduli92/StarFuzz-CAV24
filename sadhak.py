#!/usr/bin/env python3


import sys
import os
import subprocess
import time

sys.path.insert(0, 'kast/')

import ocamlgen
from kast.builder import astGenPass
import validator as vd

import psutil
import shutil

from printer import *


def format_ocaml_code(file_path):
    try:
        subprocess.run(["ocamlformat", "--enable-outside-detected-project", "--inplace", file_path], check=True)
        print(f"Successfully formatted {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error formatting {file_path}: {e}")


def kill_children(pid):
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    for child in children:
        try:
            child.kill()
        except psutil.NoSuchProcess:
            pass
    parent.kill()


def sadhak_build(signame, curr_dir):
    # build calling Makefile with ocaml file name env variable

    curr_fstar_home = os.environ['FSTAR_HOME']
    if signame in ['string_of_int']:
        # update env variables from a bashrc file
        os.environ['FSTAR_HOME'] = os.environ['FSTAR_HOME_OLD']
        os.environ['FSTAR_ULIB'] = os.environ['FSTAR_HOME'] + '/ulib'

    print_gray(f"Building {signame} with FSTAR_HOME={os.environ['FSTAR_HOME']}")
    os.system(f'ENV_INPUT_FILE={signame}.ml ENV_TARGET_NAME={signame}.exe make -f {curr_dir}/Makefile')
    os.system('mkdir -p indir')
    os.system('echo -n "AA" > indir/2byte')

    # reset env variables
    os.environ['FSTAR_HOME'] = curr_fstar_home
    os.environ['FSTAR_ULIB'] = os.environ['FSTAR_HOME'] + '/ulib'


def sadhak_check(signame, curr_dir, timeout=5):
    sadhak_build(signame, curr_dir)
    
    # get AFLDIR env variable value
    afl_dir = os.environ['AFLDIR']
    aflbin = afl_dir + "/" + "afl-fuzz" 

    # copy os environment variables
    env = os.environ.copy()
    # env["AFL_BENCH_UNTIL_CRASH"] = "1"
    env["AFL_NO_UI"] = "1"
    env["AFL_SKIP_CPUFREQ"] = "1"
    env["AFL_I_DONT_CARE_ABOUT_MISSING_CRASHES"] = "1"
    env["AFL_TRY_AFFINITY"] = "1"

    afl_fuzz_cmd = [aflbin, '-V', f'{timeout}' , '-t', '60', '-i', 'indir/', '-o', f'outdir_{signame}', '-D', f'./{signame}.exe', '@@']
    logfl = open(f'{signame}.log', 'w')
    print("\033[94m" + f"Executing command: {' '.join(afl_fuzz_cmd)}" + "\033[0m")
    subprocess.run(afl_fuzz_cmd, env=env, stdout=logfl, stderr=subprocess.PIPE)
    time.sleep(2)
    logfl.close()


def sadhak_main(input_string, bench_file=None, options=None):
    curr_dir = os.getcwd()
    if os.path.exists('logfiles'): shutil.rmtree('logfiles')
    os.makedirs('logfiles')
    os.chdir('logfiles')
    print(f'processing {input_string}')
    signame, outfile = gen_ocaml_target(input_string, bench_file)
    sadhak_check(signame, curr_dir, options.fuzz_tout)
    status = vd.validate_tests(signame, f'outdir_{signame}/default/crashes', bench_file)
    os.chdir(curr_dir)
    return outfile, status


def gen_ocaml_target(input_string, bench_file):
    # print(f'processing {input_string}')
    signame, parseTree = ocamlgen.getParseTree(input_string)
    astgen = astGenPass()
    astgen.signame = signame

    reflist, lemma = astgen.visitStart(parseTree)
    # ocamlgen.pretty_print(reflist)
    # print(f'Lemma: {lemma}')

    outfile = signame + '.ml'
    ocamlgen.dump_ocaml_target(reflist, astgen, outfile)
    # format_ocaml_code(outfile)

    return signame, outfile

def sadhak_batch(infile, options):
    with open(infile, 'r') as f:
        for line in f:
            line = line.strip()
            if line == '': continue
            sadhak_main(line, options)



