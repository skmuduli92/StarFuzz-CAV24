# StarFuzz

## Abstract

We propose StarFuzz, that allows F* ineractive theorem prover to provide better end-to-end assurance on the application— even when interfaced with the closed-box components. Verified code extracted from F* interface with external libraries containing real-life complexities—proprietary library calls, remote/cloud APIs, complex models like ML models, inline assembly, highly non-linear arithmetic, vector instructions etc. We refer to such functions/operations as closed-box components. These closed-box components are handled with the user assuming relevant lemmas about them. However, these assumed lemmas may be inconsistent due to (i) incorrect assumed specification and (ii) faulty implementation of closed-box components. To validate consistency of specification and implementation of such closed-box components, StarFuzz constructs a relevant verification condition including the closed-box components, and uses Sādhak under the hood to validate it. In our experiment, we have used StarFuzz to validate around 56 F* specifications used in many library calls that are used in F* proofs.  In our collected benchmarks from F* repository, StarFuzz discovered four bugs—one bug that revealed an error on the assumed lemmas for a closed-box function, and three bugs in the external implementations of these components.

## Artifact Evaluation

### System Requirements
- OS: Any (Ubuntu Linux is preferred)
- Memory: 8 GB
- CPU: 4 cores
- Disk capacity: at least 12 GB free space is required

We ran all experiments on an Intel(R) Xeon(R) 2.00GHz E5-2620 CPU with 32GB RAM, running Ubuntu 18.04.


### Smoke Test

To run the smoke test use the following command from `/root/starfuzz` directory. Expected run time 15 sec.

```bash
./starfuzz.py --smoke_test
```

It should print the results in form of a table as shown below after successful execution. `1.fst` and `22.fst` tests are present the `/root/starfuzz/benchmark` directory of the docker container.

```text

Results:
+--------+--------+
|  Spec  | Status |
+--------+--------+
| 1.fst  |  pass  |
| 22.fst |  fail  |
+--------+--------+
Smoke test completed.
```

If smoke test runs successfully, you may proceed for running the complete evaluation. You can find 
You can find the instructions for running the full benchmarking in the [Running Full Benchmarking](#running-full-benchmarking) section.



### Running Full Benchmarking

To run the full evaluation run the following command from `/root/starfuzz/` directory. Expected runtime 12 mins.

```bash
./starfuzz --full_bench
```

Once it runs successfully you can find the results i.e evaluation table dumped to the text file `result_table.txt`. The table layout is similar to the table shown in the **Evaluation** section of the paper. For each benchmark in the table the corresponding evaluation status is printed. The status could be `pass`, `fail` or `probe`. The interpretation of each status message is described below.

```text
pass - tool did not find any violation
fail - vaiolation found for the specification under test
probe - may be violation or false alarm which needs to be validated by probing further
```

Instructions on how to probe a false alarm is given the section [Instructions for validating generated test inputs](#Instructions-for-validating-generated-test-inputs). This step could be automated to eliminate false alarms.



### Tool Usage Instructions

To print help message and see the available options that can be passed to StarFuzz tool. Go to `/root/starfuzz` directory and run the command `./starfuzz --help`.

```bash
$ ./starfuzz.py --help

Usage: starfuzz.py [options]

StarFuzz tool for fuzzing Fstar specs.

Options:
  -h, --help            show this help message and exit
  --bench=BENCH         benchmark file
  --fuzz_tout=FUZZ_TOUT
                        fuzz timeout value in seconds
  --smoke_test          run smoke test
  --full_bench          run full test
```

Using `--bench` option user can pass the benchmark file path to run. `--fuzz_tout` is used to set the timeout for fuzzer. The `--smoke_test` and `--full_bench` can be used to run smoke test and full benchmarks respectively.



#### Project StructClaims Supported by the Artifacture

```text
|-- LICENSE
|-- Makefile                    # builds fuzz target for sadhak
|-- README.md
|-- benchmarks                  # all benchmarks are kept here
|-- extlib                      # external third-party libraries
|-- kast                        # AST definitions used in code generation
|-- ocamlgen.py                 # generates fuzz target in ocaml
|-- parse_fst.py                # parsing methods are defined here
|-- parserlib                   # parser utility to parser the fstar spec 
|-- printer.py                  
|-- sadhak.py                   # an implementation of sadhak 
|-- starfuzz.py                 # main file
`-- validator.py                # helper script for tool evaluation purpose
```




#### Instructions for validating generated test inputs
We have provided scripts to automate validation process. To run a target program with a generated test input or to investigate the false alarm user can follow the steps mentioned in this section. In the current version false alarms are not filtered out, which can be fully automated in future.

To probe the benchmark run it once again (you may increase the fuzz time using the `--fuzz_tout` parameter see `./starfuzz --help`).

```bash
./starfuzz --bench benchmark/20.fst
```

The input values could be found in `validation` directory and the generated OCaml file could be found in `/root/starfuzz/logfiles` directory. The `target` function in the OCaml file is the test driver, user can call target method with the a desired test input and see the behaviour. 

Here is an example generated OCaml code

```ocaml
(* OCAML target *)
let target x =Claims Supported by the Artifact
        let retval = FStar_Math_Lib.abs (Z.of_int x) in
        let y = Z.to_int retval in
        if not (((((not(x >= 0)) || (y = x)) && ((not(x < 0)) || (y = (0 - x)))))) then
                failwith "oops crash!!"

let () =
    Crowbar.(add_test ~name:"fuzz_abs" [int]
        (fun x ->
                target x
        ))
```

User need to call the function `target` with the generate input value to validate test input further if required as follows. This process can be used to analyze 'probe' status is generated for any benchmarks.

```ocaml

(* OCAML target *)
let target x =
        let retval = FStar_Math_Lib.abs (Z.of_int x) in
        let y = Z.to_int retval in
        if not (((((not(x >= 0)) || (y = x)) && ((not(x < 0)) || (y = (0 - x)))))) then
                failwith "oops crash!!"

let () = target 10 (* say 10 is a candidate input from the 'validation' directory*)
```

