import os,argparse,pathlib,joblib,numpy as np
from sklearn.linear_model import LogisticRegression
p=argparse.ArgumentParser(); p.add_argument('--data-uri'); p.add_argument('--epochs',type=int); a=p.parse_args(); rng=np.random.default_rng(8); X=rng.normal(size=(500,5)); y=(X[:,0]>0).astype(int); m=LogisticRegression().fit(X,y); out=pathlib.Path(os.getenv('AIP_MODEL_DIR','output/model')); out.mkdir(parents=True,exist_ok=True); joblib.dump(m,out/'model.joblib'); print(out)
