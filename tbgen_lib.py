import os

def mkdir_noexp(dir: str): 
    if not os.path.exists(dir):
        os.mkdir(dir)

def gen_vsim_makefile(top: str):
    make_str = """
# =================Project Info==========================
DUT={top}#
BENCH=\$(DUT)_tb#
VPATH=stage#
DEPENDENCY=input.txt#
RTL=rtl#
TB=tb#

#===================== Compile Flags =====================
COMPILE_FLAG:=

#===================== Optimize Flags ======================
OPT_FLAG := -floatparameters+/\$(BENCH).
OPT_FLAG += -GWAVE="\$(BENCH).vcd"

#===================== Similate Flags ====================
SIM_FLAG :=

#===================== Targets ============================
.PHONY: watch, clean, clean_all

\$(BENCH): simulate

create_lib:
    mkdir   -p  \$(VPATH)
    touch   \$(VPATH)/\$(@)
    mkdir   -p  log
    vlib.exe    ./work 

map_lib: create_lib
    touch   \$(VPATH)/\$(@)
    vmap.exe     work ./work

compile: map_lib \$(TB)/*.sv \$(RTL)/*.v \$(RTL)/*.sv
    touch   \$(VPATH)/\$(@)
    vlog.exe -l log/\$(@)_tb.log   -work    work    \$(TB)/*.sv \$(COMPILE_FLAG)
    vlog.exe -l log/\$(@)_rtl.log   -work    work    \$(RTL)/*.v

optimize: compile
    touch   \$(VPATH)/\$(@)
    vopt.exe    \$(BENCH)   +acc  -work work  -o     top_test -l log/\$@.log \$(OPT_FLAG)

simulate: optimize
    touch   \$(VPATH)/\$(@)
    vsim.exe -c -do "run -all" -l log/\$(@).log   top_test \$(SIM_FLAG)

watch: \$(BENCH).vcd
    gtkwave.exe \$(BENCH).vcd

debug: simulate
    vsim.exe work.top_test

clean:
    @rm -rf log
    @rm -rf work

clean_all: clean
    @rm -rf stage

""".format(top=top)
    return make_str

def gen_sv_top(top: str):
    svtop_str = """
//  Module: {top}_tb
//
\`timescale 1ns/1ps
module {top}_tb
    /*  package imports  */
    #(
        string WAVE
    )(

    );

    reg clk;
    /*port declare here*/

    {top} dut (.*);

    initial
    begin
        clk = 0;
        #5ns
        forever #5ns clk = ~clk;
    end

    initial
    begin
    \`ifndef VCS_SIM
        \$dumpfile(WAVE);
        \$dumpvars(0);
    \`else
        \$vcdplusfile(WAVE);
        \$vcdpluson(0);
    \`endif
    end    

    initial
    begin
        repeat(1000) @(posedge clk);
        \$display("The testbench has reached the time limit.");
        \$finish;
    end

endmodule: {top}_tb
""".format(top=top)
    return svtop_str
    
def gen_sv_tb(args):
    top_module = args.top 
    tool = args.tool
    out_dir = args.out
    mkdir_noexp(out_dir)
    mkdir_noexp(os.path.join(out_dir, "rtl"))
    mkdir_noexp(os.path.join(out_dir, "tb"))
    with open(os.path.join(out_dir, "Makefile"), 'w') as mf:
        if tool == "vsim":
            mf.write(gen_vsim_makefile(top_module))
    with open(os.path.join(out_dir, "tb/{top}_tb.sv".format(top=top_module)), 'w') as tbf:
        tbf.write(gen_sv_top(top_module))

def gen_uvm_tb(args):
    pass