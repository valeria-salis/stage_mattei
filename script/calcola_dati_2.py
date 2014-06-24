#!/usr/bin/python

import sys
from calcolatore import Calcolatore
import os
def elabora(filename, outfile):
    if os.path.exists(outfile):
        raise ValueError("Il file esiste")
    else:
        c = Calcolatore(filename)
        c.stampa_calcoli(outfile)

def main():
    elabora(sys.argv[1], sys.argv[2])

main()


























