#!/usr/bin/python

import argparse
from calcolatore import Calcolatore
import os


def elabora(filename, outfile):
    if os.path.exists(outfile):
        raise ValueError("Il file esiste")
    else:
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
