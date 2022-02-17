

class Utility:

    @staticmethod
    def rimuovi_caratteri(str, car):
        str_new = str
        for i in car:
                str_new = str_new.replace(i, "")
        return str_new
