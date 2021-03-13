import difflib
import collections


word_dist = lambda x,y : difflib.SequenceMatcher(None, x, y).ratio()

#def transform(_from):
#    to = {}

#    for val in _from:
#        if val['name'] not in to:
#            to[val['name']] = val 
#        else:
#            raise Exception("duplicate game exception")

#    return to