import sqlite3
from datetime import datetime


class db:
    
    def __init__(self):
        self.con = sqlite3.connect("ql.db")    
        self.cur = self.con.cursor()

    def create_blank(self):
        self.cur.execute("DROP TABLE IF EXISTS kitchen")
        self.cur.execute("CREATE TABLE kitchen(id INTEGER PRIMARY KEY AUTOINCREMENT, pressure REAL, temprature REAL, humidity REAL, luminance INTEGER, colour_temp INTEGER, date DATETIME)")
    
    def add_kitchen_data( self, data ):
        readings = data["readings"]
        sql = 'INSERT INTO kitchen (pressure, temprature, humidity, luminance, colour_temp, date) VALUES '
        sql += ( '( %f, %f, %f, %d, %d, "%s" )' % ( readings["pressure"], readings["temperature"], readings["humidity"], readings["luminance"], readings["color_temperature"], str(data["timestamp"]) ) )
        print( sql )
        self.cur.execute( sql )
    


#create_blank_db( my_cur )