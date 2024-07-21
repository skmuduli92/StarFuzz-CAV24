#!/usr/bin/env python3

import os
import optparse
import sadhak as sp
import parse_fst as pf
from prettytable import PrettyTable
import glob

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))


def print_table(status_map):
    table = PrettyTable()
    table.field_names = ["Spec", "Status"]

    for spec, status in status_map.items():
        if status == 0:
            status = "pass"
        elif status == 1:
            status = "fail"
        elif status == 2:
            status = "probe"
        else:
            status = "unknown"
        
        table.add_row([spec, status])

    # save table as text file
    with open("result_table.txt", "w") as f:
        f.write(str(table))

    
def run_bench(bench_file, options):
    specmap = pf.parse_fst(bench_file)
    status_map = {}
    status = 0
    for k, v in specmap.items():
        _, status = sp.sadhak_main(v, bench_file, options)
        # format_ocaml_code(outfile)
        print(f"Status for {k}: {status}")
        if status != 0: break;
    
    status_map[os.path.basename(bench_file)] = status
    return status_map

def smoke_test(options):
    status_map = {}
    sample_tests = ['benchmarks/b1.fst', 'benchmarks/b22.fst']
    for test in sample_tests:
        print("Running test: ", test)
        temp_map = run_bench(test, options)
        status_map.update(temp_map)
    
    print_table(status_map)
    print("Smoke test completed.")


def full_bench(options):
    status_map = {}
    all_tests = sorted(glob.glob("benchmarks/*.fst"), key=lambda x: int(x.split("/")[-1].split(".")[0]))
    for test in all_tests:
        print("Running test: ", test)
        temp_map = run_bench(test, options)
        status_map.update(temp_map)
    
    print_table(status_map)
    print("Full test completed.")

if __name__ == '__main__':
    cmdparser = optparse.OptionParser(description='StarFuzz tool for fuzzing Fstar specs.')

    cmdparser.add_option('--spec', help='input file')
    cmdparser.add_option('--batch', help='batch mode')
    cmdparser.add_option('--bench', help='benchmark file')
    cmdparser.add_option('--fuzz_tout', type=int, default=5, help='fuzz timeout value in seconds')

    cmdparser.add_option('--smoke_test', action='store_true', help='run smoke test')
    cmdparser.add_option('--full_bench', action='store_true', help='run full test')

    # TODO: validaiton is on by default, turn it off if needed
    cmdparser.add_option('--validation-off', action='store_true', help='turn off validation')
    (options, args) = cmdparser.parse_args()


    if options.smoke_test:
        smoke_test(options)
        exit(0)

    if options.full_bench:
        full_bench(options)
        exit(0)
    
    if options.full_bench:
        print("Running full test")
        full_bench()
        exit(0)
    

    # if any two of the arguments are provided from spec, batch, bench, then exit
    if sum([bool(options.spec), bool(options.batch), bool(options.bench)]) != 1:
        print("Please provide one of --spec, --batch, --bench")
        cmdparser.print_help()
        exit(1)

    if options.bench: run_bench(options.bench, options)       
    elif options.batch:
        infile = os.path.abspath(options.batch)
        sp.sadhak_batch(infile, options)
    elif options.spec:
        outfile = sp.sadhak_main(options.spec, options)
    else:
        cmdparser.print_help()
        exit(1)
