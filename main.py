# This is only an example of a battle that I used to test.
from core.Automata import Automata
import argparse

def get_args():
  # init
  parser = argparse.ArgumentParser()
  parser.add_argument('--img', default='syuren1')
  parser.add_argument('--sp', default='sp2')
  parser.add_argument('--party', default='1')
  args = parser.parse_args()
  print(args.img)
  return args

def main(args):
  print(type(args.party))
  party = args.party
  shiki = Automata(f"assets/{args.img}.png", f"assets/{args.sp}.png", sft=(0, 0), apl=(5, "silver"))
  # start
  shiki.quick_start()

  if party == "Buster":
    with open("./profile/Buster.txt", 'r') as file:
      code = file.read()
    exec(code)

  elif party == '0': #art
    # battle 1
    # shiki.get_current_battle()
    shiki.select_servant_skill(2)
    shiki.select_servant_skill(3,1)
    shiki.select_servant_skill(4)
    shiki.select_servant_skill(5,1)
    shiki.select_servant_skill(6,1)
    shiki.select_servant_skill(7)
    shiki.select_servant_skill(8,1)
    shiki.select_servant_skill(9,1)
    shiki.select_cards([6])
    # battle 2
    shiki.select_master_skill(3,1)
    shiki.select_servant_skill(4,1)
    shiki.select_servant_skill(5)
    shiki.select_servant_skill(6)
    shiki.select_cards([6])
    # battle 3
    #shiki.select_master_skill(3,1)
    shiki.select_servant_skill(4)
    shiki.select_servant_skill(5,1)
    shiki.select_servant_skill(6,1)
    shiki.select_cards([6])
    # finish
    shiki.finish_battle()

  elif party == '1': # buster
    # battle 1
    # shiki.get_current_battle()
    shiki.select_servant_skill(1)
    shiki.select_servant_skill(2)
    # shiki.select_servant_skill(3)
    shiki.select_servant_skill(5,1)
    shiki.select_servant_skill(6,1)
    shiki.select_servant_skill(8,1)
    shiki.select_servant_skill(9,1)
    shiki.select_cards([6])
    # battle 2
    #shiki.select_master_skill(1)
    shiki.select_servant_skill(4,1)
    shiki.select_servant_skill(7,1)
    shiki.select_servant_skill(1)
    shiki.select_cards([6])
    # battle 3
    shiki.select_servant_skill(2)
    # shiki.select_servant_skill(3)
    shiki.select_master_skill(1)
    shiki.select_master_skill(3, 2, 1)
    shiki.select_servant_skill(4)
    shiki.select_servant_skill(5,1)
    shiki.select_servant_skill(6,1)
    shiki.select_cards([6])
    # finish
    shiki.finish_battle()

  elif party == '2': # buster  + arlashu
    # battle 1
    #shiki.get_current_battle()
    shiki.select_servant_skill(3)
    shiki.select_cards([6])
    # battle 2
    shiki.select_master_skill(1)
    shiki.select_servant_skill(1)
    shiki.select_servant_skill(2)
    shiki.select_servant_skill(3)
    shiki.select_servant_skill(4, 1)
    shiki.select_servant_skill(5, 1)
    shiki.select_servant_skill(6, 1)
    shiki.select_servant_skill(7, 1)
    shiki.select_servant_skill(8, 1)
    shiki.select_servant_skill(9, 1)
    shiki.select_cards([6])
    # battle 3
    shiki.select_servant_skill(1)
    shiki.select_servant_skill(3)
    shiki.select_master_skill(3, 2, 1)
    shiki.select_servant_skill(4)
    shiki.select_servant_skill(5, 1)
    shiki.select_servant_skill(6, 1)
    shiki.select_cards([6])
    # finish
    shiki.finish_battle()

  elif party == '3':
    shiki.select_kukulkan_skill(1)
  else:
    print("party error")


if __name__=='__main__':
  main(get_args())
  