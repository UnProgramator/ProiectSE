import unittest

import utils

class Test_util_unitest(unittest.TestCase):
    
    #def test_transform(self):
    #    initival_value = [{'name':'Minecraft', 
    #                       'multiplayer':True, 
    #                       'singleplayer':True, 
    #                       'platforma':['pc', 'xbox'],
    #                       'producator':'Mojang',
    #                       'gen':['sandbox', 'suvival', 'building']},
    #                      {'name':'Dark Souls', 
    #                       'multiplayer':True, 
    #                       'singleplayer':True, 
    #                       'platforma':['pc', 'xbox', 'ps'],
    #                       'producator':'FromSoftware',
    #                       'gen':['souls-like', 'hack-n-slash', 'combat']},
    #                       {'name':'Mortal shell', 
    #                       'multiplayer':False, 
    #                       'singleplayer':True, 
    #                       'platforma':['pc', 'xbox', 'ps'],
    #                       'producator':'Cold Symetry',
    #                       'gen':['souls-like', 'hack-n-slash', 'combat']}
    #                      ]
    #    expected_result={
    #                     'Minecraft': {'name':'Minecraft', 
    #                                   'multiplayer':True, 
    #                                   'singleplayer':True, 
    #                                   'platforma':['pc', 'xbox'],
    #                                   'producator':'Mojang',
    #                                   'gen':['sandbox', 'suvival', 'building']},
    #                     'Dark Souls': {'name':'Dark Souls', 
    #                                   'multiplayer':True, 
    #                                   'singleplayer':True, 
    #                                   'platforma':['pc', 'xbox', 'ps'],
    #                                   'producator':'FromSoftware',
    #                                   'gen':['souls-like', 'hack-n-slash', 'combat']},
    #                      'Mortal shell': {'name':'Mortal shell', 
    #                                   'multiplayer':False, 
    #                                   'singleplayer':True, 
    #                                   'platforma':['pc', 'xbox', 'ps'],
    #                                   'producator':'Cold Symetry',
    #                                   'gen':['souls-like', 'hack-n-slash', 'combat']}}
    #    resulted_value = utils.transform(initival_value)
    #    self.assertEqual(expected_result, resulted_value)
    pass

if __name__ == '__main__':
    unittest.main()
    exit(0)
