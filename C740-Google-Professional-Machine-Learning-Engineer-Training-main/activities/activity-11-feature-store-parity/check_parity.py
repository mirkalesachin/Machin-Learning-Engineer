import pandas as pd,argparse
p=argparse.ArgumentParser(); p.add_argument('--offline'); p.add_argument('--online'); a=p.parse_args(); x=pd.read_csv(a.offline).merge(pd.read_csv(a.online),on='customer_id',suffixes=('_off','_on')); cols=['txn_count_1h','spend_7d','risk_score'];
for c in cols: x[c+'_diff']=x[c+'_on']-x[c+'_off']
print(x[['customer_id']+[c+'_diff' for c in cols]].to_string(index=False))
