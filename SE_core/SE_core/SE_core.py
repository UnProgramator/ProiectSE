from utils import *
from typing import Union, Dict, List
from bd import knoledge_type, knoledge_base, load_db, check_db




def process(inputData: Dict[str, Union[str, int, bool, List[Union[str, int, bool]]]], limit:int) -> knoledge_type:
    """
    process an imput for a client and calculate which games are recomended

    Parameters:
    inputData (dict[str, union[str, int, bool, list[union[str, int, bool]]]]): the request from the client

    Return:
    (knoledge_type) the games and description
    """
    scoreboard={}
    result=[]

    for attributes in knoledge_base:
        score = get_score(inputData, attributes)
        if score < 0.0:
            continue
        if score in scoreboard:
            scoreboard[score]+=attributes
        else:
            scoreboard[score]=list(attributes)
    
    nr=0 

    for i in sorted(scoreboard):
        nr+=len(lst)
        
        result += scoreboard[i].sort()

        if(nr>=limit):
            break
    return result[0:limit]


def get_score(inputData: Dict[str, Union[str, int, bool, List[Union[str, int, bool]]]], obj: knoledge_type) -> float:
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
    pass



if __name__=="__main__":
    exit(0)