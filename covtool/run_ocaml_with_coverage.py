import subprocess
import os




# Step 1: Compile the OCaml program with bisect_ppx
# OCAMLPATH=/home/smuduli/git/everest/FStar/lib ocamlfind opt -package crowbar -package fstar.lib -package afl-persistent -linkpkg -g 
compile_command = "OCAMLPATH=/home/smuduli/git/everest/FStar/lib ocamlfind opt -package bisect_ppx -package crowbar -package fstar.lib -package afl-persistent -o example -linkpkg example.ml"
subprocess.run(compile_command, shell=True)

compile_command = "OCAMLPATH=/home/smuduli/git/everest/FStar/lib ocamlfind opt -package bisect_ppx -package crowbar -package fstar.lib -package afl-persistent -o driver -linkpkg driver.ml"
subprocess.run(compile_command, shell=True)

def run_test(inputs_file):
    # Step 2: Run the OCaml program with each input file
    ocaml_run_command = f"./example {inputs_file}"    
    # run command and store output in a string
    output = subprocess.run(ocaml_run_command, shell=True, capture_output=True)
    # print output
    outval = output.stdout.decode('utf-8')

    # extract string between output:<string>
    outval = outval.split("output:")[0]
    # if outval contains output substring, then split it and take the first part
    if "output" in outval:
        outval = outval.split("output")[1]
        # take first line of outval
        outval = outval.split("\n")[0]
        outval = outval[1:-1]
        print("outval:", outval)
        # outval = outval.split("end")[0]
        return outval
    
    pass

def generate_coverage_report():
    # Step 3: Generate the coverage report
    generate_report_command = "bisect-ppx-report html"
    subprocess.run(generate_report_command, shell=True)

    # Step 4: Open the coverage report in a web browser
    report_path = os.path.join("_coverage", "index.html")
    if os.path.exists(report_path):
        open_browser_command = f"open {report_path}"  # Adjust for your platform
        subprocess.run(open_browser_command, shell=True)
    else:
        print("Coverage report not found.")


if __name__ == "__main__":
    # Assume you have binary input files named input1.bin, input2.bin, etc.
    # input_files = ["input1.bin", "input2.bin", "input3.bin"]

    # get input file names from the input directory which begins with "id"
    input_files = [f for f in os.listdir("/home/smuduli/git/starfuzz/logfiles/outdir/default/queue") if f.startswith("id")]

    # get full path of each input file
    input_files = [os.path.join("/home/smuduli/git/starfuzz/logfiles/outdir/default/queue", f) for f in input_files]
    
    # print input files line by line
    print("Input files:")
    for input_file in input_files:
        print(input_file)

    # Run tests with coverage for each input file
    output_str = []
    for input_file in input_files:
        output = run_test(input_file)
        if output:
            output_str.append(output)


    print("output string:", output_str)



    for inval in output_str:
    # Step 2: Run the OCaml program with each value in output_str
        ocaml_run_command = f"./driver {inval}"
        print("run command:", ocaml_run_command)
        # run command and store output in a string
        subprocess.run(ocaml_run_command, shell=True)
            
    
    # Generate coverage report after all tests are executed
    # generate_coverage_report()

