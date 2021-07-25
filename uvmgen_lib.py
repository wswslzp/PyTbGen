import os 

def mkdir_noexp(dir: str): 
    if not os.path.exists(dir):
        os.mkdir(dir)

def gen_uvm_dir_tree(out_dir: str):
    sub_dirs = ['agent', 'env', 'sim', 'tb', 'test']
    for sub_dir in sub_dirs:
        mkdir_noexp(os.path.join(out_dir, sub_dir))
        # TODO: Auto gen agent dir

def gen_uvm_seq_item(out_dir, ag_name: str):
    with open(os.path.join(out_dir, ag_name + "_seq_item.sv")) as tran_f:
        ret = "\nclass {ag}_seq_item extends uvm_sequence_item;".format(ag=ag_name)
        ret += "\n"
        ret += "\nendclass"
        tran_f.write(ret)
    pass 

def gen_uvm_seq(out_dir, ag_name: str):
    pass 

def gen_uvm_seqr(out_dir, ag_name: str):
    pass 

def gen_uvm_driver(out_dir, ag_name: str):
    pass 

def gen_uvm_monitor(out_dir, ag_name: str):
    pass 

def gen_uvm_ent(out_dir, ag_name: str):
    pass

