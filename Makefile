
ifndef FSTAR_HOME
$(error FSTAR_HOME is not set, please set the environment variable)
endif

include $(FSTAR_HOME)/examples/Makefile.include
include $(FSTAR_ULIB)/ml/Makefile.include

ENV_TARGET_NAME?=test_fuzz.exe

OCAML_FILE = ${ENV_INPUT_FILE}
TARGET_NAME = ${ENV_TARGET_NAME}

out: $(OCAML_FILE)
	$(OCAMLOPT) -afl-instrument -thread -package fstar.lib -package afl-persistent -package crowbar -linkpkg $(OCAML_FILE) -o $(TARGET_NAME)

fuzz: test_fuzz.exe
	 $(AFLDIR)/afl-fuzz -V 120 -t 100 -i indir/ -o outdir -D ./$(TARGET_NAME) @@

clean:
	rm -rf out *~ *.exe *.checked *.cm* *.o
