#!/usr/bin/python

import sys
from calcolatore import Calcolatore

def elabora(filename, outfile):
    c = Calcolatore(filename)
    c.stampa_calcoli(outfile)

def main():
    elabora(sys.argv[1], sys.argv[2])

main()


























