import xml.etree.cElementTree as ET
import re
import itertools
import csv

path = r'C:\Users\Balaji\Desktop\Drug.xml'

drug = open(path,'r',encoding='utf-8')
drugData = str(drug.read())
drug.close()

tree=ET.fromstring(drugData)


ns = {'webs':'http://www.drugbank.ca'}

count=0
database ={}

for elem in tree.findall('./{http://www.drugbank.ca}drug'):
    name = elem.find('./{http://www.drugbank.ca}name')
    inhibitors=[]
    for elem2 in elem.findall('./{http://www.drugbank.ca}targets/{http://www.drugbank.ca}target'):
        action = elem2.find('./{http://www.drugbank.ca}actions/{http://www.drugbank.ca}action')
        organism = elem2.find('./{http://www.drugbank.ca}organism')
        if action is None or organism is None:
            continue
        elif action.text is 'inhibitor' or 'inhibitory allosteric modulator' or 'inhibitor, competitive' and organism.text is 'Human':
            gene = elem2.find('./{http://www.drugbank.ca}name')
            if gene!=None:
                inhibitors.append(gene.text)
    database[name.text]=inhibitors

database = {k:v for k,v in database.items() if v!=[]}

reactions = []
with open('genes .csv','rt') as f:
    reader=csv.reader(f)
    for row in reader:
        reactions.append(row[4])


for t,v in database.items():
    l = [t1 for t1 in v for g in reactions if g.strip(' ').lower().find(t1.strip('').lower())!=-1]
    database.update({t:set(l)})


database = {k:v for k,v in database.items() if v!=set([])}
drugL = [k for k,v in database.items()]
print(drugL)
print(len(drugL))

#print(database)
#print(len(database))