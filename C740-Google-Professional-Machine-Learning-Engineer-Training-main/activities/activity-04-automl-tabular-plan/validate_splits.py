import pandas as pd,sys
df=pd.read_csv(sys.argv[1]); assert df.target.notna().all(); print(df.groupby('split').size()); print(df.dtypes)
