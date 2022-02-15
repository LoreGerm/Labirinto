


class Labirinto:

    def __init__(self, giocatore, stanze):
        self.__giocatore = giocatore
        self.__stanze = stanze  # DIZIONARIO

    def get_giocatore(self):
        return self.__giocatore

    def get_stanza(self):
        return self.__stanze
    

    def controlla(self):
        if self.__giocatore.get_punti_vita() != 0:
            x = self.__giocatore.comandi()
            if x == '1':
                if self.__stanze[self.__giocatore.get_posizione()].get_manuale() == True:
                    print('Hai vinto')
                else:
                    print("Non c'è nulla")

            elif x == '2':
                print("Numero porte:  ", self.__stanze[self.__giocatore.get_posizione()].get_uscite())
                x = self.__giocatore.muovi()
            
        else:
            print('Hai perso')