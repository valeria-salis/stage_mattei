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
        if colonna in c.fieldnames:
            vmax = max(colonna)
			elif not colonna in c.fieldnames:
				raise ValueError()
		return max1
			
	

    def calcola_minimo(self, colonna):
        if colonna in c:
		vmin = min(colonna)
	elif not colonna in c:
		raise ValueError ()
	return vmin 

    def calcola_media(self, colonna):
<<<<<<< HEAD
        
=======
			if colonna in c.fieldnames:
			somma = sum(colonna)		
			elif not colonna in c.fieldnames:
				raise ValueError()
			media1 = float(somma) / len(colonna)
		return media1
>>>>>>> 554226f618cb4a0dde5039c02f69801b149939f6

    def stampa_calcoli(self, filename):
        """
        Per ogni colonna, calcola massimo, minimo e media e stampate il tutto su un file
        """
        raise NotImplementedError()
