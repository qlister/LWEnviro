import sqlite3




class SQLiteDB:
    def __init__(self):
        self.con = sqlite3.connect("ql.db")    
        self.cur = con.cursor()

    def create_blank(my_cur):
        self.cur.execute("DROP TABLE IF EXISTS kitchen")
        self.cur.execute("CREATE TABLE kitchen(id INTEGER PRIMARY KEY AUTOINCREMENT, temprature REAL, humidity REAL, date DATETIME)")
    
    def add_kitchen_data( data ):
        sql = 'INSERT INTO kitchen (temprature, humidity, date) VALUES '
        sql += '( 21.0, 40.1, "' + now.strftime( '%Y-%m-%dT%H:%M') + '" )'
        print( sql )
        self.cur.execute( sql )
    


#create_blank_db( my_cur )