import csv

class Calcolatore(object):
    
    def __init__(self, filename, colonne_accettate=None):
        self.datifile = dict()
        with open(filename) as f:
            c = csv.DictReader(f, delimiter = "\t")
            for h in c.fieldnames: 
                if (colonne_accettate and h in colonne_accettate) or not colonne_accettate:
                    self.datifile[h] = []
                
            for r in c:
                for k,v in r.iteritems():
                    if (colonne_accettate and k in colonne_accettate) or not colonne_accettate:
                        self.datifile[k].append(float(v))

    def calcola_massimo(self, colonna):
        raise NotImplementedError()

    def calcola_minimo(self, colonna):
        raise NotImplementedError()

    def calcola_media(self, colonna):
        raise NotImplementedError()

    def stampa_calcoli(self, filename):
        """
        Per ogni colonna, calcola massimo, minimo e media e stampate il tutto su un file
        """
        raise NotImplementedError()
