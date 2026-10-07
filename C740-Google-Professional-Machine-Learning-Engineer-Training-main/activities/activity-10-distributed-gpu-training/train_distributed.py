import os,argparse
p=argparse.ArgumentParser(); p.add_argument('--epochs',type=int,default=1); a=p.parse_args();
try:
 import torch,torch.distributed as dist
 dist.init_process_group('gloo'); rank=dist.get_rank(); x=torch.tensor([float(rank+1)]); dist.all_reduce(x); print({'rank':rank,'sum':x.item(),'epochs':a.epochs}); dist.destroy_process_group()
except Exception as e: print('distributed smoke-test diagnostic:',type(e).__name__,str(e))
