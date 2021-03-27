import json
#from utils import transform
from typing import Union, Dict, List, Iterable

knoledge_type = Dict[str, Union[str, int, List[str]]]

gereKnoledgeBase=None

knoledge_base: Dict[str, knoledge_type]=None

def load_games() -> None:
    """
    load the database into the global variable knoledge_base
    """
    global knoledge_base
    with open("knoledge_base/knoledge_base.json") as json_file:
        #knoledge_base = transform(json.load(json_file))
        knoledge_base = json.load(json_file)

def load_genres() ->None:
    global gereKnoledgeBase
    with open("knoledge_base/genre2attributes.json") as json_file:
        gereKnoledgeBase = json.load(json_file)

def save_bd() -> None:
    global knoledge_base
    with open("knoledge_base/knoledge_base.json", "w") as json_file:
        json_file.write(json.dumps(knoledge_base, indent=5, sort_keys=False))

def save_gen_to_att(genuri_list) -> None:
    with open('knoledge_base\genre2attributes.json','w') as kb:
         json.dump(genuri_list,kb,indent = 5, sort_keys=False)        

def check_db()-> None:
    """
    Test implementation function
    """
    global knoledge_base
    print(knoledge_base)
