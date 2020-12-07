import unittest
import quick_tools as tool

class TestQuickToolsMethods(unittest.TestCase):

    def setUp(self):
        #Creation de BDD
        self.db_path = 'test_chat.db'
        tool.create_db(self.db_path)

    def tearDown(self):
        #Suppression de BDD
        tool.delete_db(self.db_path)

    def test_add_room(self):
        add_room(self.db_path,'room0','public')
        self.assertEqual(tool.get_rooms(self.db_path), ['room0']))

    def test_add_user(self):
        add_user('quick_chat.db','yann.c',0,0,'password')
        self.assertEqual(tool.get_rooms(self.db_path), )

    # def test_get_rooms(self):
    #
    #     self.assertEqual(tool.get_rooms(db_path), ['room0'])

   # def test_delete_room(self):

   # def test_delete_user(self):

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
