class Squadra(object):
    def __init__(self, nome):
        self.nome = nome
        self.vinte = 0
        self.pareggiate = 0
        self.perse = 0
        self.goal_fatti = 0
        self.goal_subiti = 0

    def punti(self):
        # 3 punti per vittoria, 1 per pareggio, 0 per sconfitta
        raise NotImplementedError()


class Girone(object):
    def __init__(self, nome, squadre):
        self.nome = nome
        self.squadre = squadre
        self.risultati = []

    def stampa_classifica(self):
        raise NotImplementedError()

    def aggiungi_partita(self, partita):
        raise NotImplementedError()

class FonteDati(object):
    IndirizzoServer = 'http://live.mobileapp.fifa.com/api/'
    API_TEAMS = 'wc/teams'
    API_ROUND = 'wc/matches'

    def __init__(self, indirizzo):
        self.indirizzo = indirizzo

    def _traduci_partita(self, fifa_dict):
        # Il servizio FIFA ci restituisce molte informazioni che non ci servono,
        # in un formato loro. Pescate i campi che vogliamo e costriute un dict
        # per il nostro utilizzo:
        # { 'squadra1': nome, 'squadra2': nome, 'goal1': x, 'goal2': y }
        # Campi FIFA: "c_HomeTeam_en", "c_AwayTeam_en", "n_HomeGoals", "n_AwayGoals"
        raise NotImplementedError()

    def get_partite_di_girone(self, nome_girone):
        # Interroga http://live.mobileapp.fifa.com/api/wc/matches.
        # Interpreta il contenuto della risposta come JSON
        # Filtra le partite per appartenenza al girone richiesto. Per esempio,
        # Girone "A" -> "c_Phase_en":"Group A"
        # Traduci le partite con self._traduci_partita
        # Restituisci le partite nel nostro formato (vedi _traduci_partita)
        raise NotImplementedError()

    def get_squadre_del_girone(self, nome_girone):
        # Interroga http://live.mobileapp.fifa.com/api/wc/teams.
        # Filtra per 'c_Group'
        # Costruisci una Squadra per ogni risultato, prendendo il nome
        # dal campo 'c_Team_en'.
        # Restituisci le squadre.
        raise NotImplementedError()

class Applicazione(object):
    def __init__(self):
        self.girone = None # Girone
        self.server = None # Crea la FonteDati qui

    def scansione_argomenti(self):
        raise NotImplementedError()

    def _costruisci_girone(self, nome_girone):
        # Costruisci Girone
        # Recupera Squadre dal server e aggiungi al Girone quelle che gli appartengono
        # return girone
        raise NotImplementedError()

    def esegui(self):
        # Scansiona argomenti. Recupera nome del girone fornito
        # Crea Girone (con self._costruisci_girone) e assegnalo a self.girone
        # Recupera partite; Aggiungile al girone con Girone.aggiungi_partita
        raise NotImplementedError()


class Squadra(object):
    def __init__(self, nome):
        self.nome = nome
        self.vinte = 0
        self.pareggiate = 0
        self.perse = 0
        self.goal_fatti = 0
        self.goal_subiti = 0

    def punti(self):
        # 3 punti per vittoria, 1 per pareggio, 0 per sconfitta
        raise NotImplementedError()


class Girone(object):
    def __init__(self, nome, squadre):
        self.nome = nome
        self.squadre = squadre
        self.risultati = []

    def stampa_classifica(self):
        raise NotImplementedError()

    def aggiungi_partita(self, partita):
        raise NotImplementedError()

class FonteDati(object):
    IndirizzoServer =  'http://live.mobileapp.fifa.com/api/'
    API_TEAMS = 'wc/teams'
    API_ROUND = 'wc/matches'

    def __init__(self, indirizzo):
        self.indirizzo = indirizzo

    def _traduci_partita(self, fifa_dict):
        # Il servizio FIFA ci restituisce molte informazioni che non ci servono,
        # in un formato loro.  Pescate i campi che vogliamo e costriute un dict
        # per il nostro utilizzo:
        # { 'squadra1': nome, 'squadra2': nome, 'goal1': x, 'goal2': y }
        # Campi FIFA: "c_HomeTeam_en", "c_AwayTeam_en", "n_HomeGoals", "n_AwayGoals"
        raise NotImplementedError()

    def get_partite_di_girone(self, nome_girone):
        # Interroga http://live.mobileapp.fifa.com/api/wc/matches.
        # Interpreta il contenuto della risposta come JSON
        # Filtra le partite per appartenenza al girone richiesto.  Per esempio,
        # Girone "A" -> "c_Phase_en":"Group A"
        # Traduci le partite con self._traduci_partita
        # Restituisci le partite nel nostro formato (vedi _traduci_partita)
        raise NotImplementedError()

    def get_squadre_del_girone(self, nome_girone):
        # Interroga http://live.mobileapp.fifa.com/api/wc/teams.
        # Filtra per 'c_Group'
        # Costruisci una Squadra per ogni risultato, prendendo il nome
        # dal campo 'c_Team_en'.
        # Restituisci le squadre.
        raise NotImplementedError()

class Applicazione(object):
    def __init__(self):
        self.girone = None  # Girone
        self.server = None  # Crea la FonteDati qui

    def scansione_argomenti(self):
        raise NotImplementedError()

    def _costruisci_girone(self, nome_girone):
        # Costruisci Girone
        # Recupera Squadre dal server e aggiungi al Girone quelle che gli appartengono
        # return girone
        raise NotImplementedError()

    def esegui(self):
        # Scansiona argomenti.  Recupera nome del girone fornito
        # Crea Girone (con self._costruisci_girone) e assegnalo a self.girone
        # Recupera partite; Aggiungile al girone con Girone.aggiungi_partita
        raise NotImplementedError()


def main():
    a = Applicazione()
    a.esegui()

main()
