import requests
import csv
#import EnzymeAffected

reactions = []
with open('genes .csv','rt') as f:
    reader=csv.reader(f)
    for row in reader:
        reactions.append(row[23])

#print(reactions)


d = {'kappa':['APPA'],'dss':['ghhf12','AOC2'],'asas':['CUBN','AOC1']}
#d2={}
#l=[]

for t,v in d.items():
    l = [t1 for t1 in v for g in reactions if t1 == g]
    d.update({t:set(l)})


d = {k:v for k,v in d.items() if v!=set([])}

print(d)