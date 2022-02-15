

from classi.giocatore import Giocatore
from classi.labirinto import Labirinto
from classi.stanza import Stanza


g = Giocatore('afafa')

s = Stanza('parcheggio', 'Aula gialla', None, 'Atrio', None)

stanze = {s.get_nome():s}

#print(s.get_uscite())

l = Labirinto(g, stanze)

l.controlla()