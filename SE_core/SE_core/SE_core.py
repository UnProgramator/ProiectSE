from utils import *
from typing import Union, Dict, List
import bd
import random
import SE_web

genres=None
not_genres=[]

def process(inputData: bd.knoledge_type, limit:int) -> bd.knoledge_type:
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

    print("prod",inputData["producator"])

    for game_attributes in bd.knoledge_base:
        score = get_score(inputData, game_attributes)
        if score < 0.0:
            continue
        if score in scoreboard:
            scoreboard[score]+=[game_attributes]
        else:
            scoreboard[score]=[game_attributes] 
    
    nr=0 

    for i in sorted(scoreboard, reverse=True):
        nr+=len(scoreboard[i])
        scoreboard[i].sort(key=lambda x: x['nume'])
        result += scoreboard[i]
        if(nr>=limit):
            break
        
    return result[:limit]


def get_score(inputData: bd.knoledge_type, obj: bd.knoledge_type) -> float:
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
    nr = 0

    if inputData['pegi'] < obj['pegi']:
        # daca copilul are varsta specificata si o are mai mica ca jocul, se returneaza -100 din start
        return -100

    if inputData['platforma'] is not None:
        #daca exita preferinta de platforma si acest joc nu corespunde, dam -100, nu recomandam jocuri de ps pt cine cere de ps
        if set(inputData['platforma']).intersection(set(obj['platforma'])) == set():
            return -100

    if obj['pegi'] <=7:
        if inputData['pegi'] - obj['pegi'] <= 3:
            score+=100
        elif inputData['pegi'] - obj['pegi'] < 7:
            score+=100*int(obj['pegi']/inputData['pegi']*0.7)
        else:
            score+=10
    elif obj['pegi'] <= 13:
        if inputData['pegi'] - obj['pegi'] < 3:
            score += 100
        elif inputData['pegi'] - obj['pegi'] < 5:
            score+=70
        elif inputData['pegi'] - obj['pegi'] < 8:
            score+=30
        else:
            score+=10
    else:
        score+=100
    
    nr+=1

    if inputData['multiplayer'] is not None:
        if inputData['multiplayer'] == obj['multiplayer']: score += 100
        else: score -= 50
        nr+=1

    if inputData['singleplayer'] is not None:
        if inputData['singleplayer'] == obj['singleplayer']: score += 100
        else: score -= 50
        nr+=1

    if inputData['producator'] is not None and inputData['producator'] != []:
        for pr in inputData['producator']:
            if word_dist(pr, obj['producator']) > 0.8:
                score+= 200
                nr+=1
                break

    if genres is not None:
        intnum = len(set(genres).intersection(obj['gen']))
        if intnum == 0:
            score -= 100    
        else:
            if set(not_genres).intersection(obj['gen']) !=set():
                score -= 200
            score+=100*intnum
        nr+=(intnum if intnum !=0 else 1)

    return int(score/nr)

def getGenres(inputAttributes:List[str]):
    def compare(list, target):
        for att in target:
            if type(att) is dict:
                if att['not'] in list:
                    return False;
            else:
                if att not in list:
                    return False
        return True

    posible_genres = set()

    for partial_rule in bd.gereKnoledgeBase['partials']:
        for rulename in partial_rule:
            if compare(inputAttributes, partial_rule[rulename]):
                inputAttributes+=[rulename]

    for genre_rule in bd.gereKnoledgeBase['games types']:
        for genre in genre_rule:
            rules = genre_rule[genre]
            if(compare(inputAttributes, rules)):
                posible_genres.add(genre)
    posible_genres = list(posible_genres)
    no_genres=[]
    for i in range(len(posible_genres)):
        if posible_genres[i][0:4] == 'no-':
            no_genres+=posible_genres[i][3:]
    return posible_genres, no_genres

def callback(preferences:bd.knoledge_type):
    global genres
    global not_genres
    genres,not_genres = getGenres(preferences['questions'])
    if genres == []:
        genres = None
    return process(preferences, 20)

def main():
    bd.load_games()
    bd.load_genres()
    #check_db()
    #l = process({"multiplayer":True, "singleplayer":True, "pegi":12, 'producator':['Blizzards']}, 10)
    #print_list(l)

if __name__ == '__main__':
    main()