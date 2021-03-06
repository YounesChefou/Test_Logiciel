import sqlite3

def get_room(db_path, room_name):
	if (isinstance(room_name, str) == False):
		raise Exception('room_name doit être sous la forme de string');

	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'SELECT room_name FROM Rooms WHERE room_name=?;'

	rooms = cursor.execute(sql,(room_name,))

	rooms = [room[0] for room in rooms]

	return rooms

def get_rooms(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'SELECT room_name FROM Rooms;'

	rooms = cursor.execute(sql ).fetchall()

	rooms = [room[0] for room in rooms]

	return rooms

def add_room(db_path, room_name, room_type):
	if (isinstance(room_name, str) == False):
		raise Exception('room_name doit être sous la forme de string');

	if (isinstance(room_type, str) == False):
		raise Exception('room_type doit être sous la forme de string');

	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'INSERT INTO Rooms (room_name,room_type) VALUES (?,?)'

	cursor.execute(sql,(room_name, room_type))
	connect.commit()


def delete_room(db_path, room_name):
	if (isinstance(room_name, str) == False):
		raise Exception('room_name doit être sous la forme de string');

	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'DELETE FROM Rooms WHERE room_name=?'

	cursor.execute(sql,(room_name,))
	connect.commit()

def delete_rooms(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'DELETE FROM Rooms'

	cursor.execute(sql)
	connect.commit()


def get_users(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'SELECT user_name FROM Users;'

	users = cursor.execute(sql ).fetchall()

	users = [user[0] for user in users]

	return users


def add_user(db_path, user_name, user_role, user_rights, user_password):
	if (isinstance(user_name, str) == False):
		raise Exception('user_name doit être sous la forme de string');

	if (isinstance(user_password, str) == False):
		raise Exception('user_password doit être sous la forme de string');


	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'INSERT INTO Users (user_name, user_role, user_rights, user_password) VALUES (?,?,?,?)'

	cursor.execute(sql,(user_name, user_role, user_rights, user_password))
	connect.commit()


def delete_user(db_path, user_name):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'DELETE FROM Users WHERE user_name=?'

	cursor.execute(sql,(user_name,))
	connect.commit()

def create_db(db_path):
	connect = sqlite3.connect(db_path)

	cursor = connect.cursor()

	cursor.execute('CREATE TABLE Rooms ([id_room] INTEGER PRIMARY KEY,[room_name] text UNIQUE, [room_type] text)')
	cursor.execute('CREATE TABLE Users ([id_user] INTEGER PRIMARY KEY,[user_name] text UNIQUE, [user_role] integer, [user_rights] integer, [user_password] text)')

	connect.commit()

def delete_db(db_path):
	connect = sqlite3.connect(db_path)

	cursor = connect.cursor()

	cursor.execute('DROP TABLE IF EXISTS Rooms')
	cursor.execute('DROP TABLE IF EXISTS Users')

	connect.commit()

#Db creation :

# db_path = 'quick_chat.db'
#
# create_db(db_path)
#
# add_user('quick_chat.db','yann.c',0,0,'password')
# add_room('quick_chat.db','room0','public')
#
# print(get_users(db_path))
# print(get_rooms(db_path))
# delete_user(db_path,'yann.c')
# print(get_users(db_path))
