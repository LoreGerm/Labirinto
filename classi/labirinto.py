



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
                print('\n')
                print(self.__giocatore.get_nome(), ' ti trovi in ',self.__giocatore.get_posizione())
                print('Hai ', self.__giocatore.get_punti_vita(), ' vite')
                print('Cosa vuoi fare')
                comando = self.__giocatore.comandi()
                if comando == '1':
                    if self.__stanze[self.__giocatore.get_posizione()].get_manuale() == True:
                        print('\n')
                        print('HAI VINTO')
                        break
                    else:
                        print('\n')
                        print("Non c'è nulla")

                elif comando == '2':
                    esci = False
                    print('\n')
                    print("Direzioni disponibili")
                    direzione = self.__giocatore.muovi(self.__stanze[self.__giocatore.get_posizione()].get_uscite())
                    for i in self.__stanze[self.__giocatore.get_posizione()].get_uscite().keys():
                        if i == direzione:
                            self.__giocatore.set_posizione(self.__stanze[self.__giocatore.get_posizione()].get_uscite()[i])
                            esci = True
                            break
                    if esci == False:
                        print('Non valido')
                elif comando == '3':
                    fine = True    
            else:
                fine = True
                print('Hai perso')