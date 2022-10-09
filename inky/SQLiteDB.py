import sqlite3
#from datetime import datetime


class db:
    
    def __init__(self):
        self.con = sqlite3.connect("ql.db")    
        self.cur = self.con.cursor()

    def create_blank(self):
        self.cur.execute("DROP TABLE IF EXISTS kitchen")
        self.cur.execute("CREATE TABLE kitchen(id INTEGER PRIMARY KEY AUTOINCREMENT, pressure REAL, temprature REAL, humidity REAL, luminance INTEGER, colour_temp INTEGER, uid VARCHAR(20), date DATETIME)")
        self.cur.execute("DROP TABLE IF EXISTS urban_outdoor")
        self.cur.execute("CREATE TABLE urban_outdoor(id INTEGER PRIMARY KEY AUTOINCREMENT, pressure REAL, temprature REAL, humidity REAL, pm1 INTEGER, pm2_5 INTEGER, pm10 INTEGER, noise REAL, voltage REAL, uid VARCHAR(20), date DATETIME)")
    
    def add_kitchen_data( self, data ):
        if data['model']  == 'indoor':
            readings = data["readings"]
            sql = 'INSERT INTO kitchen (pressure, temprature, humidity, luminance, colour_temp, uid, date) VALUES '
            sql += ( '( %f, %f, %f, %d, %d, "%s", "%s" )' % ( readings["pressure"], readings["temperature"], readings["humidity"], readings["luminance"], readings["color_temperature"], data["uid"], str(data["timestamp"]) ) )
#            print( sql )
            self.cur.execute( sql )
            self.con.commit()
        else:
            print( "Unexpected model in add_kitchen_data" )
            print ( data )
        
    def add_urban_data( self, data ):
        if data['model']  == 'urban':
            readings = data["readings"]
            sql = 'INSERT INTO urban_outdoor (pressure, temprature, humidity, pm1, pm2_5, pm10, noise, voltage, uid, date) VALUES '
            sql += ( '( %f, %f, %f, %d,%d, %d, %f, %f, "%s", "%s" )' % ( readings["pressure"], readings["temperature"], readings["humidity"], readings["pm1"], readings["pm2_5"], readings["pm10"], readings["noise"], readings["voltage"], data["uid"], str(data["timestamp"]) ) )
#            print( sql )
            self.cur.execute( sql )
            self.con.commit()
        else:
            print( "Unexpected model in add_urban_data" )
            print ( data )
    


#create_blank_db( my_cur )