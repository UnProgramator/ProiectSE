import difflib


word_dist = lambda x,y : difflib.SequenceMatcher(None, x, y).ratio()


