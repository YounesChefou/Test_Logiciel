import unittest
import sqlite3
import quick_tools as tool

class TestQuickToolsMethods(unittest.TestCase):

    def setUp(self):
        #Creation de BDD
        self.db_path = 'test_chat.db'
        self.connect = sqlite3.connect(self.db_path)
        self.cursor = self.connect.cursor()
        tool.create_db(self.db_path)

    def tearDown(self):
        #Suppression de BDD
        tool.delete_db(self.db_path)

    def test_get_room(self):
        tool.add_room(self.db_path, 'room_get', 'public')
        self.assertEqual(tool.get_room(self.db_path, 'room_get'), ['room_get'])

    def test_get_rooms(self):
        tool.add_room(self.db_path,'room0','public')
        self.assertEqual(tool.get_rooms(self.db_path), ['room0'])

    def test_add_room(self):
        #python peut raise des exceptions :
        # https://ongspxm.gitlab.io/blog/2016/11/assertraises-testing-for-errors-in-unittest/
        # ici ça peut etre utile de verifier que les arguments passés sont bien des string
        tool.add_room(self.db_path,'room0','public')
        tool.add_room(self.db_path,0,'public')
        self.assertEqual(tool.get_rooms(self.db_path), ['room0'])
        #with self.assertRaises(Exception) :
        #string exception raised dans la def de la fonction sur quick_tools.py

    def test_get_users(self):
        tool.add_user(self.db_path,'yann.c',0,0,'password')
        self.assertEqual(tool.get_users(self.db_path), ['yann.c'])

    def test_add_multiple_rooms(self):
        tool.add_room(self.db_path,'room0','public')
        tool.add_room(self.db_path,'room1','public')
        self.assertEqual(tool.get_rooms(self.db_path), ['room0','room1'])

    def test_add_user(self):
        tool.add_user(self.db_path,'yann.c',0,0,'password')
        self.assertEqual(tool.get_users(self.db_path),['yann.c'])

    #DOUBLON
    def test_delete_room(self):
        tool.add_room(self.db_path,'room0','public')
        tool.add_room(self.db_path,'room1','public')
        tool.delete_room(self.db_path, 'room0')
        #print(tool.get_rooms(self.db_path))
        self.assertEqual(tool.get_rooms(self.db_path), ['room1'])

    def test_delete_rooms(self):
        tool.add_room(self.db_path,'room0','public')
        tool.add_room(self.db_path,'room1','public')
        tool.delete_rooms(self.db_path)
        self.assertEqual(tool.get_rooms(self.db_path), [])

    def test_delete_room(self):
       tool.add_room(self.db_path, 'room_del', 'public')
       self.assertEqual(tool.get_room(self.db_path, 'room_del'), ['room_del'])
       tool.delete_room(self.db_path, 'room_del')
       self.assertEqual(tool.get_room(self.db_path, 'room_del'), [])



    def test_delete_user(self):
        tool.add_user(self.db_path,'yann.c',0,0,'password')
        tool.add_user(self.db_path,'bob',0,0,'123456')
        tool.delete_user(self.db_path, 'yann.c')
        #print(tool.get_users(self.db_path))
        self.assertEqual(tool.get_users(self.db_path), ['bob'])


    def test_create_db(self):
        #Sélectionne toutes les tables existantes d'une base de données https://www.ipgirl.com/702/comment-puis-je-verifier-dans-sqlite-si-une-table-existe.html
        sql = "SELECT name FROM sqlite_master WHERE type='table'"
        #print(self.cursor.execute(sql).fetchall())
        self.assertEqual(self.cursor.execute(sql).fetchall(), [('Rooms',), ('Users',)])

    def test_delete_db(self):
        tool.delete_db(self.db_path)
        sql = "SELECT name FROM sqlite_master WHERE type='table'"
        #print(self.cursor.execute(sql).fetchall())
        self.assertEqual(self.cursor.execute(sql).fetchall(), [])



if __name__ == '__main__':
    unittest.main()
