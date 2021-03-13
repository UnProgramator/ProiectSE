from utils import *
from typing import Union, Dict, List
import bd
from bd import knoledge_type, load_db, check_db
import random
import SE_web


def process(inputData: knoledge_type, limit:int) -> knoledge_type:
    """
    process an imput for a client and calculate which games are recomended

    Parameters:
    inputData (dict[str, union[str, int, bool, list[union[str, int, bool]]]]): the request from the client

    Return:
    (knoledge_type) the games and description
    """
    scoreboard={}
    result=[]

    if type(limit) is not int:
        raise Exception("limit must be an integer")

    for game_attributes in bd.knoledge_base:
        score = get_score(inputData, game_attributes)
        if score < 0.0:
            continue
        if score in scoreboard:
            scoreboard[score]+=[game_attributes]
        else:
            scoreboard[score]=[game_attributes]
    
    nr=0 

    for i in sorted(scoreboard):
        nr+=len(result)

        scoreboard[i].sort(key=lambda x: x['nume'])

        result += scoreboard[i]

        if(nr>=limit):
            break
    return result[0:limit]


def get_score(inputData: knoledge_type, obj: knoledge_type) -> float:
    """
    A function that verify if an value for an attribute is pressent in a game attributes and return a score
    
    Parameters:
    knoledge_attr (str): use to transmite the attribute name 
            - ex: 'multiplayer'
    knoledge_val  (union[str, int, bool]): transmite a value 
            for the specified attribute; for list transmite a value a time
            -ex: true / "pc" / 10?

    Return:
    (int) the score
    """
    score = 0

    if inputData['pegi'] != -1 and inputData['pegi'] < obj['pegi']:
        # daca copilul are varsta specificata si o are mai mica ca jocul, se returneaza -100 din start
        return -100

    if inputData['multiplayer'] == obj['multiplayer']: score += 100
    else: score -= 50

    if inputData['singleplayer'] == obj['singleplayer']: score += 100
    else: score -= 50

    if inputData['producator'] is not None:
        for pr in inputData['producator']:
            if word_dist(pr, obj['producator']) > 80:
                score+= 100
                break

    return score

def callback(preferences):
    return process(preferences, 10)

def main():
    load_db()
    #check_db()
    l = process({"multiplayer":True, "singleplayer":True, "pegi":12, 'producator':['Blizzards']}, 10)
    print_list(l)

if __name__ == '__main__':
    main()