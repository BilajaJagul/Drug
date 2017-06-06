from lxml import etree
from xml.dom import minidom
from bs4 import BeautifulSoup
import requests
import xml.etree.cElementTree as ET
import re
import itertools
import csv
import _pickle as cpickle

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
        organism = elem2.find('./{http://www.drugbank.ca}organism')
        for action in elem2.findall('./{http://www.drugbank.ca}actions/{http://www.drugbank.ca}action'):
            if action is None or organism is None:
                continue
            elif action.text == 'inhibitor' or action.text == 'inhibitory allosteric modulator' or action.text == 'inhibitor, competitive' or action.text == 'antagonist' and organism.text == 'Human':
                gene = elem2.find('./{http://www.drugbank.ca}polypeptide/{http://www.drugbank.ca}gene-name')
                if gene!=None:
                    inhibitors.append(gene.text)
    database[name.text]=inhibitors


database = {k:v for k,v in database.items() if v!=[]}

reactions = []
with open('genes .csv','rt') as f:
    reader=csv.reader(f)
    for row in reader:
        reactions.append(row[23])


for t,v in database.items():
    l = [t1 for t1 in v for g in reactions if t1 == g]
    database.update({t:set(l)})


database = {k:v for k,v in database.items() if v!=set([])}
drugL = [k for k,v in database.items()]

#print(drugL)
#print(len(drugL))