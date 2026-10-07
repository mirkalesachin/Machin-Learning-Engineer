import requests,argparse
p=argparse.ArgumentParser(); p.add_argument('--base-url'); a=p.parse_args(); print(requests.get(a.base_url+'/health').json()); r=requests.post(a.base_url+'/predict',json={'features':[4,8,3]}); print(r.status_code,r.json()); assert r.status_code==200
