




class Giocatore:
    __nome = ""
    __punti_vita = 10
    __posizione = ""

    def __init__(self, nome):
        self.__nome = nome 
        self.__posizione = "parcheggio"

    def set_nome(self, nome):
        self.__nome = nome 

    def set_punti_vita(self, vita):
        self.__punti_vita = vita
    
    def set_posizione(self, pos):
        self.__posizione = pos


    def get_nome(self):
        return self.__nome

    def get_punti_vita(self):
        return self.__punti_vita
    
    def get_posizione(self):
        return self.__posizione

    
    def muovi(self):
        print('1 - Nord')
        print('2 - Sud')
        print('3 - Est')
        print('4 - Ovest')
        x = input('Dove vuoi andare:   ')
        if x == '1' or x == '2' or x == '3' or x == '4':
            self.__punti_vita -= 1
            return x
        else:
            return 'Comando non valido'


    def comandi(self):
        x = 0
        while x != 3:
            print('1 - Guarda')
            print('2 - Vai')
            print('3 - Esci dal gioco')
            x = input('Cosa voui fare:   ')

            if x == '1' or x == '2' or x == '3':
                return x
            else:
                return 'Comando non valido'