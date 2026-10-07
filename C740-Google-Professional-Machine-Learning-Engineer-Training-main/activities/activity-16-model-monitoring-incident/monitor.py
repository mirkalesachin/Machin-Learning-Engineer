import pandas as pd,numpy as np,argparse,json
p=argparse.ArgumentParser(); p.add_argument('--baseline'); p.add_argument('--current'); p.add_argument('--out'); a=p.parse_args(); b=pd.read_csv(a.baseline); c=pd.read_csv(a.current); bins=np.linspace(0,1,6); bp=np.histogram(b.feature,bins)[0]/len(b)+1e-6; cp=np.histogram(c.feature,bins)[0]/len(c)+1e-6; psi=float(np.sum((cp-bp)*np.log(cp/bp))); tpr={};
for g,x in c.groupby('group'):
 pos=x[x.outcome==1]; tpr[g]=float((pos.prediction==1).mean()) if len(pos) else None
r={'psi':psi,'accuracy':float((c.prediction==c.outcome).mean()),'tpr_by_group':tpr,'p95_ms':float(c.latency_ms.quantile(.95))}; json.dump(r,open(a.out,'w'),indent=2); print(r)
