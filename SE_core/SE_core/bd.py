import json
from utils import transform
from typing import Union, Dict, List, Iterable

knoledge_type = Dict[str, Union[str, int, Iterable['knoledge_type']]]

knoledge_base: Dict[str, knoledge_type]=None

def load_db() -> None:
    """
    load the database into the global variable knoledge_base
    """
    with open("") as json_file:
        knoledge_base = transform(json.load(json_file))

def check_db()-> None:
    """
    Test implementation function
    """
    print(knoledge_base)