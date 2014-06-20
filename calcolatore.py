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
        if colonna in self.datifile:
            vmax = max(self.datifile[colonna])
        else:
            raise ValueError()
        return vmax

    def calcola_minimo(self, colonna):
        if colonna in self.datifile:
            vmin = min(self.datifile[colonna])
        else:
            raise ValueError ()
        return vmin

    def calcola_media(self, colonna):
        if colonna in self.datifile:
            somma = sum(self.datifile[colonna])
        else:
            raise ValueError()
        media1 = float(somma) / len(self.datifile[colonna])
        return media1


    def stampa_calcoli(self, filename):
        statistiche = open(filename, 'w')
        fieldnames = ["nome_colonna","massimo","minimo", "media"]
        csvwriter = csv.DictWriter(statistiche, delimiter = "\t", fieldnames=fieldnames)
        for k, v in self.datifile.iteritems():
            row = {
                "nome_colonna" : k,
                "massimo" : self.calcola_massimo(k),
                "minimo" : self.calcola_minimo(k),
                "media" : self.calcola_media(k)
            }
            csvwriter.writerow(row)
        file.close()











        raise NotImplementedError()
