#!/usr/bin/python

import csv
import sys
def carica(file_input):
    dati = []
    with open(file_input) as fo:
        fo_csv = csv.DictReader(fo, delimiter="\t")
        for r in fo_csv:
            dati.append(r)
    return dati 

def elabora(tabella):
    maxx=[]
    minn=[]
    for r in tabella:
        maxx.append(int(r['max qual']))
        minn.append(int(r ['min qual']))
        
    smax = sum(maxx)
    smin = sum(minn)
    m1 = float(smax) / len(maxx)
    m2 = float(smin) / len(minn)
    vmin=min(minn)
    vmax=max(maxx)
    print "il valore minimo:",vmin, "Media dei valori:",m2
    print "il valore massimo:",vmax,"Media dei valori:",m1

def main():
    print "gli argomenti sono", sys.argv
    t=carica(sys.argv[1])
    elabora(t)
    

