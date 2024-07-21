#!/usr/bin/env python3

import os
import argparse

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))


def get_cbfun_libs(bench):
    cbfun_libs = {}
    with open(bench, 'r') as file:
        lines = file.readlines()
        starfuzz_lines = [line for line in lines if line.startswith('@starfuzz')]
        for line in starfuzz_lines:
            # print(line.strip())
            libinfo = line.strip().split(':')
            # print(libinfo)
            funname, libname = libinfo[1].strip().split(' ')
            libname = libname.strip('[').strip(']')
            print("Function name: {}, Lib name: {}".format(funname, libname))
            cbfun_libs[funname] = libname

    return cbfun_libs

def get_cb_specs(bench, cbfuns):
    # find cbl declarations in the file
    # it starts with val <cbl> = ...
    cb_specs = {}
    with open(bench, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            for cb in cbfuns:
                if line.startswith('val {}'.format(cb)):
                    # print("Found spec for  {}:: {}".format(cb, line))
                    cb_specs[cb] = line
                    break

    return cb_specs

def parse_fst(bench):
    infile = os.path.abspath(bench)
    print("input bench file: {}".format(infile))
    cbfun_libs = get_cbfun_libs(infile)
    cbfuns = [cb[0] for cb in cbfun_libs]
    print(cbfun_libs)
    cbfuns = cbfun_libs.keys()
    specs = get_cb_specs(infile, cbfuns)
    return specs

if __name__ == '__main__':
    cmdparser = argparse.ArgumentParser(description='StarFuzz tool for fuzzing Fstar specs.')    
    cmdparser.add_argument('--bench', help='benchmark file')    
    args = cmdparser.parse_args()

    if args.bench:
        specs = parse_fst(args.bench)
        print(specs)
    else:
        cmdparser.print_help()
        exit(1)
