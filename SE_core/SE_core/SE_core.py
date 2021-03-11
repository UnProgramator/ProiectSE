from utils import *
from typing import dict, union
from bd import knoledge_type, knoledge_base, load_db, check_db




def process(inputData: dict[str, union[str, int, bool, list[union[str, int, bool]]]]) -> knoledge_type:
    """
    process an imput for a client and calculate which games are recomended

    Parameters:
    inputData (dict[str, union[str, int, bool, list[union[str, int, bool]]]]): the request from the client

    Return:
    (knoledge_type) the games and description
    """
    pass

def get_score(knoledge_attr: str, knoledge_val: union[str, int, bool], obj: knoledge_type) -> float:
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