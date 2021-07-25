# Auto Testbench Generation

## Overview 
```bash
usage: tbgen [-h] [-t TOP] [-o OUT] [-m {svtb,uvmtb}] [--tool {vsim,vcs}]

optional arguments:
  -h, --help            show this help message and exit
  -t TOP, --top TOP     Top module
  -o OUT, --out OUT     Output dir
  -m {svtb,uvmtb}, --method {svtb,uvmtb}
  --tool {vsim,vcs}     The simulation tool
```

## Current Features
Now the supported features are:
* Generate `svtb` systemverilog testbench.
* Generate `vsim` questasim simulation script.

## TODO
Implement all the feature listed in the Usage.
