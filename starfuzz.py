#!/usr/bin/env python3

import os
import optparse
import sadhak as sp
import parse_fst as pf
from prettytable import PrettyTable
import glob

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))


def print_table(status_map, save_to_file=False):
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

    if not save_to_file:
        print("\nResults:")
        print(table)
    else:    
        # save table as text file
        with open("result_table.txt", "w") as f:
            f.write(str(table))
        print("Results saved to 'result_table.txt'")

    
def run_bench(bench_file, options):
    specmap = pf.parse_fst(bench_file)
    status_map = {}
    status = 0
    for k, v in specmap.items():
        _, status = sp.sadhak_main(v, bench_file, options)
        # format_ocaml_code(outfile)
        if status != 0: break;
    
    status_map[os.path.basename(bench_file)] = status
    return status_map

def smoke_test(options):
    status_map = {}
    sample_tests = ['benchmarks/1.fst', 'benchmarks/22.fst']
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
    
    print_table(status_map, save_to_file=True)
    print("Full test completed.")

if __name__ == '__main__':
    cmdparser = optparse.OptionParser(description='StarFuzz tool for fuzzing Fstar specs.')

    cmdparser.add_option('--bench', help='benchmark file')
    cmdparser.add_option('--fuzz_tout', type=int, default=5, help='fuzz timeout value in seconds')
    cmdparser.add_option('--smoke_test', action='store_true', help='run smoke test')
    cmdparser.add_option('--full_bench', action='store_true', help='run full test')

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
    

    if options.bench: 
        run_bench(options.bench, options)
        exit(0)

    cmdparser.print_help()
    exit(1)
