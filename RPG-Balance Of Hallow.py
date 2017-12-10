#Jogo de RPG baseado em RPG
#v1.1
#Rodará somente em CMD
import random
from time import sleep

class heroi:  #personagens principais

    ativo = True
    status_neg = ['burn', 'poison', 'blinded']
    status_pos = ['mightguard', 'haste', 'defup', 'atkup']
    def __init__(self, hp, lvl, str, int, agi, defe, mdef, matk, atk, gold):
        self.hp = hp
        self.lvl = lvl
        self.str = str
        self.int = int
        self.agi = agi
        self.gold = gold
        self.defe = defe
        self.mdef = mdef
        self.matk = matk
        self.atk = atk

    def get_hp(self):
        print("hp atual: " + self.hp)
    def get_lvl(self):
        print("Nível: " + self.lvl)
    def get_str(self):
        print("Força: " + self.str)
    def get_int(self):
        print("Inteligência: " +self.int)
    def get_agi(self):
        print("Agilidade: " +self.agi)
    def get_gold(self):
        print("Ouro: " +self.gold)




'''princ = (input("Entre com o nome do personagem: "))
princ = heroi(320, 1, 5, 1, 1, 1, 1, 0, 3, 1500)
princ.get_lvl()'''