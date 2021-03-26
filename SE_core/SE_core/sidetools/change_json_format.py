import bd
from utils import print_list

def transform1():
    for joc in bd.knoledge_base:
        val=0;
        if type(joc["pegi"]) is not str: 
            continue
        for c in joc["pegi"]:
            if c == '+':
                break
            val = val*10 + int(c)
        joc["pegi"]=val



if __name__ == "__main__":
    bd.load_games()
    transform1()
    print_list(bd.knoledge_base)
    if input() == 'y':
        bd.save_bd()
