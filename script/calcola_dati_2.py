#!/usr/bin/python

import sys
from calcolatore \
    import Calcolatore
import argparse

def elabora(filename, outfile):
    c = Calcolatore(filename)
    c.stampa_calcoli(outfile)

def main():
    parser = argparse.ArgumentParser(description="Calcola le statistiche da un file in input")
    parser.add_argument("--input", help="file in input",
                        type=str, required=True)
    parser.add_argument("--output", help="file di output",
                        type=str, required=True)
    args= parser.parse_args()
    elabora(args.input, args.output)
main()
