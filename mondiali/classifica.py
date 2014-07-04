import argparse
import requests
import csv
class Squadra(object):
    def __init__(self, nome):
        self.nome = nome
        self.vinte = 0
        self.pareggiate = 0
        self.perse = 0
        self.goal_fatti = 0
        self.goal_subiti = 0
    def __str__(self):
        return self.nome + ' ' + str(self.punti())

    def punti(self):
        punteggio = self.vinte * 3 + self.pareggiate
        return punteggio
class Girone(object):
    def __init__(self, nome, nomi_squadre):
        self.nome = nome
        self.squadre = dict()
        for a in nomi_squadre:
            self.squadre[a] = Squadra(a)
    def stampa_classifica(self):
        a = sorted(self.squadre.values(),key=lambda s: -1*s.punti())
        for c in a:

            print c
    def aggiungi_partita(self, partita):
        nome_squadra = partita ['squadra1']
        squadra1 = self.squadre[nome_squadra]
        nome_squadra = partita ['squadra2']
        squadra2 = self.squadre[nome_squadra]
        squadra1.goal_fatti = squadra1.goal_fatti + partita['goal1']
        squadra1.goal_subiti = squadra1.goal_subiti + partita['goal2']
        squadra2.goal_fatti += partita['goal2']
        squadra2.goal_subiti += partita ['goal1']
        if partita['goal1'] > partita ['goal2']:
            squadra1.vinte += 1
            squadra2.perse += 1
        elif partita['goal2'] > partita ['goal1']:
            squadra2.vinte += 1
            squadra1.perse += 1
        else:
            squadra1.pareggiate += 1
            squadra2.pareggiate += 1
class FonteDati(object):
    IndirizzoServer = 'http://live.mobileapp.fifa.com/api/'
    API_TEAMS = 'wc/teams'
    API_ROUND = 'wc/matches'


    def _traduci_partita(self, fifa_dict):
        row = {
                'squadra1': fifa_dict['c_HomeTeam_en'],
                'squadra2': fifa_dict['c_AwayTeam_en'],
                'goal1' :  fifa_dict['n_HomeGoals'],
                'goal2' :  fifa_dict['n_AwayGoals'],
                }
        return row
    def get_partite_di_girone(self, nome_girone):
        partite = []
        id_girone = "Group " + nome_girone
        r = requests.get('http://live.mobileapp.fifa.com/api/wc/matches')
        r = r.json()
        for c in r['data']['group']:
            if id_girone == c['c_Phase_en']:
                row = self._traduci_partita(c)
                partite.append(row)
        return partite


    def get_squadre_del_girone(self, nome_girone):
            squadra = []
            r = requests.get("http://live.mobileapp.fifa.com/api/wc/teams")
            r = r.json()
            for c in r['data']:
                if nome_girone == c["c_Group"]:
                    squadra.append(c['c_Team_en'])
            return squadra

class Applicazione(object):
    def __init__(self):
        self.girone = None # Girone
        self.server = FonteDati() # Crea la FonteDati qui

    def scansione_argomenti(self):
        parser = argparse.ArgumentParser(description="Crea la classifica")
        parser.add_argument("--nome_girone", help="nome del girone", type=str, required=True)
        args = parser.parse_args()
        return args.nome_girone
    def _costruisci_girone(self, nome_girone):
        squadre = self.server.get_squadre_del_girone(nome_girone)
        girone = Girone(nome_girone, squadre)
        return girone
    def esegui(self):
        nome_girone = self.scansione_argomenti()
        girone = self._costruisci_girone(nome_girone)
        partite = self.server.get_partite_di_girone(nome_girone)
        for c in partite:
            girone.aggiungi_partita(c)
        girone.stampa_classifica()

def main():
    a = Applicazione()
    a.esegui()
if __name__ == '__main__':
    main()
