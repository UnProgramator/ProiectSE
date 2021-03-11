

knoledge_type = dict[str, union[str, int, Interable('knoledge_type')]]

knoledge_base: list[knoledge_type]

def loaddb() -> None:
    """
    load the database into the global variable knoledge_base
    """