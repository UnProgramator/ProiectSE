import json

knoledge_type = dict[str, union[str, int, Interable('knoledge_type')]]

knoledge_base: list[knoledge_type]

def load_db() -> None:
    """
    load the database into the global variable knoledge_base
    """
    with open("") as json_file:
        knoledge_base=json.load(json_file)

def check_db()-> None:
    """
    Test implementation function
    """
    print(knoledge_base)