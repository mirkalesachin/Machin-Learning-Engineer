import pandas as pd,argparse,hashlib,json,pathlib
p=argparse.ArgumentParser(); p.add_argument('--input'); p.add_argument('--profile-only',action='store_true'); p.add_argument('--out-dir',default='output'); a=p.parse_args(); df=pd.read_csv(a.input)
print(df.describe(include='all').to_string())
if not a.profile_only:
 out=pathlib.Path(a.out_dir); out.mkdir(exist_ok=True); df=df.drop_duplicates('event_id'); df.loc[df.amount<0,'amount']=None; df.amount=df.amount.fillna(df.amount.median()); df.to_csv(out/'features.csv',index=False); json.dump({'rows':len(df),'sha256':hashlib.sha256((out/'features.csv').read_bytes()).hexdigest()},open(out/'manifest.json','w'),indent=2)
