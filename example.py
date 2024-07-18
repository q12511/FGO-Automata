# This is only an example of a battle that I used to test.
from core.Automata import Automata
# init
shiki = Automata("assets/event.png", "assets/sp2.png")
# start
shiki.quick_start()
# battle 1
shiki.select_servant_skill(5)
shiki.select_servant_skill(6)
shiki.select_servant_skill(7)
shiki.select_cards([7])
# battle 2
shiki.select_servant_skill(8)
shiki.select_cards([8])
# battle 3
# shiki.toggle_master_skill()
shiki.select_master_skill(2, 1)
shiki.select_servant_skill(1)
shiki.select_servant_skill(2)
shiki.select_cards([6])
# finish
shiki.finish_battle()
