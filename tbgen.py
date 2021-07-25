#!/usr/bin/python3
import argparse as ap
import tbgen_lib

parser = ap.ArgumentParser(prog="tbgen")

parser.add_argument("-t", "--top", type=str, help="Top module")
parser.add_argument("-o", "--out", type=str, help="Output dir", default="verif")
parser.add_argument("-m", "--method", choices=["svtb", "uvmtb"], default="svtb")
parser.add_argument("--tool", choices=["vsim", "vcs"], help="The simulation tool", default="vsim")

args = parser.parse_args()

if args.method == "svtb":
    tbgen_lib.gen_sv_tb(args)
elif args.method == "uvmtb":
    tbgen_lib.gen_uvm_tb(args)
