


class Stanza:

    def __init__(self, nome, nord, sud, est, ovest, manuale=False):
        self.__nome = nome
        self.__uscita_N = nord
        self.__uscita_S = sud
        self.__uscita_E = est
        self.__uscita_O = ovest
        self.__manuale = manuale


    def get_uscite(self):
        x = {}
        if self.__uscita_N != None:
            x['Nord'] = self.__uscita_N

        if self.__uscita_S != None:
            x['Sud'] =  self.__uscita_S

        if self.__uscita_E != None:
            x['Est'] = self.__uscita_E

        if self.__uscita_O != None:
            x['Ovest'] = self.__uscita_O

        return x


    def get_manuale(self):
        return self.__manuale

    def get_nome(self):
        return self.__nome

    def set_manuale(self,m):
        self.__manuale = m

    def __repr__(self):
        return self.__nome