import argparse,sys
p=argparse.ArgumentParser(); p.add_argument('--auc',type=float); p.add_argument('--p95-ms',type=float); p.add_argument('--fairness-gap',type=float); a=p.parse_args(); failures=[]
if a.auc<.82: failures.append('AUC below 0.82')
if a.p95_ms>300: failures.append('p95 latency above 300 ms')
if a.fairness_gap>.05: failures.append('fairness gap above 0.05')
print('BLOCK' if failures else 'PASS',failures); sys.exit(bool(failures))
