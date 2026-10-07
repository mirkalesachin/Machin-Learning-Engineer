cases=[(30,10,5,55),(34,18,1,47),(38,29,2,31)]
for tp,fp,fn,tn in cases:
 p=tp/(tp+fp); r=tp/(tp+fn); f=2*p*r/(p+r)
 print({'precision':round(p,3),'recall':round(r,3),'f1':round(f,3)})
