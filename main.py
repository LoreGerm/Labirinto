
import random
from classi.giocatore import Giocatore
from classi.labirinto import Labirinto
from classi.stanza import Stanza

nome = input('Inserisci il tuo nome:    ')
g = Giocatore(nome)

s = Stanza('Parcheggio', None, 'Atrio', None, None)
s1 = Stanza('Atrio', 'Parcheggio', 'Presidenza', 'Stanza Relax', 'Segreteria')
s2 = Stanza('Segreteria', None, 'Aula azzurra', 'Atrio', 'Aula gialla')
s3 = Stanza('Aula gialla', None, None, 'Segreteria', None)
s4 = Stanza('Aula azzurra', 'Segreteria', None, None, None)
s5 = Stanza('Presidenza', 'Atrio', None, None, None)
s6 = Stanza('Stanza Relax', None, None, None, 'Atrio')


# MANUALE RANDOM
manuale = random.randint(0, 6)
l = [s,s1,s2,s3,s4,s5,s6]
l[manuale].set_manuale(True)

# PENITENZA RANDOM
penitenza = random.randint(1, 6)
l[penitenza].set_penitenza(True)

# POZIONE RANDOM
penitenza = random.randint(0, 6)
l[penitenza].set_penitenza(True)


stanze = {s.get_nome():s, s1.get_nome():s1, s2.get_nome():s2, s3.get_nome():s3, s4.get_nome():s4, s5.get_nome():s5, s6.get_nome():s6}


l = Labirinto(g, stanze)

l.gioca()