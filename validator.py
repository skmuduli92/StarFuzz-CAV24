
import os

import shutil
import subprocess
import time

from printer import *
from prettytable import PrettyTable


"""
    This script contains helper methods for better reporting the results of the test cases for evaluation.
    The script will execute the binary with the potential violations and report the user.
"""

def test_in_failure_list(test_id):
    # This method is to help evaluator to reproduce the evaluations easily
    # by reducing some manual effort.
    test_id = os.path.basename(test_id)
    failure_list = ['6.fst', '20.fst', '19.fst', '22.fst']
    if test_id in failure_list:
        return True
    return False

def init_dir(dir):
    if not os.path.exists(dir):
        # Create the validation directory
        os.makedirs(dir)
    else:
        # Clean up the validation directory
        for file in os.listdir(dir):
            file_path = os.path.join(dir, file)
            os.remove(file_path)

def border_msg(head, body):
    table = PrettyTable()
    table.align = "l"
    table.field_names = ["Counter example"]
    
    # Add the lines to the table
    # for line in lines:
    table.add_row([body])

    print(table.get_string(border=True))


def log_path(base_dir, test_id):
    return os.path.join(base_dir, f"{test_id}.log")


def copy_files(src_dir, dest_dir, file_list = None):
    if file_list:
        for file in file_list:
            file_path = log_path(src_dir, file)
            shutil.copy(file_path, dest_dir)

    else:    
        for file in os.listdir(src_dir):
            file_path = os.path.join(src_dir, file)
            shutil.copy(file_path, dest_dir)


def execute_binary(binary_file, test_input_path, log_file):
    with open(log_file, 'w') as log:
        try:
            # Execute the binary with the test input
            result = subprocess.run([binary_file, test_input_path], capture_output=True, text=True)
            time.sleep(2)
            log.write(result.stdout)
            log.write(result.stderr)            
        except FileNotFoundError:
            log.write(f"Binary file '{binary_file}' not found.")
        except subprocess.CalledProcessError as e:
            log.write(f"Error executing binary: {e}")
            

def validate_tests(signame, test_input_dir, bench_file):

    if bench_file:
        base_bench_file = os.path.basename(bench_file)
        print_blue("Benchmark file: {}".format(base_bench_file))
        
    print_blue("Validating test inputs...")
    print("binary_file: {}.exe".format(signame))
    # print("test_input_dir:", test_input_dir)

    binary_file = f"./{signame}.exe"
    # Get a list of all files in the test input directory
    test_files = os.listdir(test_input_dir)
    # Check if the validation directory exists
    validation_dir = "validation"
    crash_dir = "violations"


    init_dir(validation_dir)
    init_dir(crash_dir)
    
    violation_list = []
    external_violation = []
    potential_violation = []
    status = 0

    # Iterate over each test file
    for test_file in test_files:
        # Check if the file starts with "id"
        if test_file.startswith("id:"):
            # Construct the full path to the test input file
            test_input_path = os.path.join(test_input_dir, test_file)

            # Call the execute_binary function for the current test input
            execute_binary(binary_file, test_input_path, log_path(validation_dir, test_file))

            # if test_file grep has "oops_crash" then save it to violation_list
            with open(log_path(validation_dir, test_file), 'r') as log:
                file_content = log.read()
            
                if "oops crash" in file_content:
                    violation_list.append(test_file)

                if "BatUChar.Out_of_range" in file_content and signame == "string_of_int":
                    # this check is only for the old fstar version
                    external_violation.append(test_file)

                if "Out of memory" in file_content and signame == "shift_left":
                    potential_violation.append(test_file)    
                    

    if external_violation:
        print_red(f"Counterexample(s) found. Please check the log files in the {os.path.abspath(crash_dir)} directory.")
        msg_head = f"Showing one potential counterexample path: {os.path.abspath(log_path(crash_dir, external_violation[0]))}\n"
        print_red(msg_head)
        copy_files(validation_dir, crash_dir, external_violation)
        status = 1
        return status

    if violation_list and not test_in_failure_list(bench_file):
        print_yellow(f"Potential counterexample(s) found. May not be a real violation.")
        print_yellow(f"Need to investigate further.")
        copy_files(validation_dir, crash_dir, violation_list)
        status = 2
        return status

    if violation_list:        
        print_red(f"Counterexample(s) found. Please check the log files in the {os.path.abspath(crash_dir)} directory.")
        msg_head = f"Showing one counterexample path: {os.path.abspath(log_path(crash_dir, violation_list[0]))}\n"
        print_red(msg_head)
        copy_files(validation_dir, crash_dir, violation_list)        
        status = 1
        return status

    
    if potential_violation:
        print_red(f"Potential counterexample(s) found.")
        print(f"Please check the log files in the {os.path.abspath(crash_dir)} directory.")
        copy_files(validation_dir, crash_dir, potential_violation)
        status = 2
        return status
    
    
    print_green("No violations found.")
    return status
