




class Giocatore:
    __nome = ""
    __punti_vita = 10
    __posizione = ""

    def __init__(self, nome):
        self.__nome = nome 
        self.__posizione = "Parcheggio"

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

    
    def muovi(self, direzioni):
        
        for i in direzioni:
            if i == 'Nord':
                print('1 - ', direzioni[i])
            elif i == 'Sud':
                print('2 - ', direzioni[i])
            elif i == 'Est':
                print('3 - ', direzioni[i])
            elif i == 'Ovest':
                print('4 - ', direzioni[i])

        x = input('Dove vuoi andare:   ')
        if x == '1':
            return 'Nord'
        elif x == '2':
            return 'Sud'
        elif x == '3':
            return 'Est'
        elif x == '4':
            return 'Ovest'
        else:
            return 'Comando non valido'


    def comandi(self):
        print('1 - Cerca nella stanza')
        print('2 - Cambia stanza')
        print('3 - Esci dal gioco')
        x = input('Cosa voui fare:   ')

        if x == '1' or x == '2' or x == '3':
            return x
        else:
            return 'Comando non valido'