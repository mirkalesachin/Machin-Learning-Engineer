import csv,json,argparse
p=argparse.ArgumentParser(); p.add_argument('--requirements'); p.add_argument('--out'); a=p.parse_args()
rows={r['requirement']:r['value'] for r in csv.DictReader(open(a.requirements))}
scores={'bigquery_ml':78,'automl':84,'custom_training':82}
result={'requirements':rows,'scores':scores,'selected':max(scores,key=scores.get),'headroom_qps':round(float(rows['peak_qps'])*1.3)}
json.dump(result,open(a.out,'w'),indent=2)
print(result)
