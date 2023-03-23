from RngAirport import main #Vivek did this
import sqlite3
import random

def connect(self):
        self.conn = sqlite3.connect('skunkworks.db')
        self.cursor = self.conn.cursor()
def breakConn(self):
    #Terminates connection
        self.connection.close()
        self.cursor.close()
def __init__(self):
    self.cursor.execute(f"INSERT INTO airports (icao_code,iata_code,city,country,lat_deg,lat_min,lat_sec,lat_dir,lon_deg,lon_min,lon_sec,lon_dir,altitude,lat_decimal,lon_decimal) VALUES ('{random.choice(results)}','{random.choice(results2)}','{random.choice(results3)}','{random.choice(results4)}', '{random.choice(results5)}','{random.choice(results6)}', '{random.choice(results7)}', '{random.choice(results8)}')")

    time.sleep(5)
