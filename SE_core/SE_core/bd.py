import json
#from utils import transform
from typing import Union, Dict, List, Iterable

knoledge_type = Dict[str, Union[str, int, List[str]]]

knoledge_base: Dict[str, knoledge_type]=None

def load_db() -> None:
    """
    load the database into the global variable knoledge_base
    """
    global knoledge_base
    with open("../../knoledge_base/knoledge_base.json") as json_file:
        #knoledge_base = transform(json.load(json_file))
        knoledge_base = json.load(json_file)

def check_db()-> None:
    """
    Test implementation function
    """
    global knoledge_base
    print(knoledge_base)