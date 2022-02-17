



class Labirinto:

    def __init__(self, giocatore, stanze):
        self.__giocatore = giocatore
        self.__stanze = stanze  # DIZIONARIO

    def get_giocatore(self):
        return self.__giocatore

    def get_stanza(self):
        return self.__stanze
    

    def gioca(self):
        fine = False
        while fine == False:
            if self.__giocatore.get_punti_vita() != 0:
                print(self.__giocatore.get_posizione())
                print('Vite:  ',self.__giocatore.get_punti_vita())
                x = self.__giocatore.comandi()
                if x == '1':
                    if self.__stanze[self.__giocatore.get_posizione()].get_manuale() == True:
                        print('Hai vinto')
                        break
                    else:
                        print("Non c'è nulla")

                elif x == '2':
                    esci = False
                    print("Porte:  ", self.__stanze[self.__giocatore.get_posizione()].get_uscite())
                    x = self.__giocatore.muovi()
                    for i in self.__stanze[self.__giocatore.get_posizione()].get_uscite().keys():
                        if i == x:
                            
                            self.__giocatore.set_posizione(self.__stanze[self.__giocatore.get_posizione()].get_uscite()[i])
                            esci = True
                            break
                    if esci == False:
                        print('Non valido')
                elif x == '3':
                    fine = True    
            else:
                fine = True
                print('Hai perso')