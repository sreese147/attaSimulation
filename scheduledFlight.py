"""Sabrina Reese
Cmdr Schenk
march 15 2023
progress check 1
scheduled flight
period 5 cs50 ap"""
import time
import random
from faker import Faker
from faker_airtravel import AirTravelProvider
import sqlite3
import mysql.connector



def main():

    connection = sqlite3.connect('s.db')
    cursor = connection.cursor()

    fake = Faker()
    fake.add_provider(AirTravelProvider)
    

    status= ["Awaiting", "Boarding", "Departing", "InFlight - OnTime", "InFlight - Late", "Landed - On Time", "Landed - Late", "Cancelled", "Delayed", "Unknown"]
    
    for i in range(1,5):
        query = """INSERT INTO scheduled_flights (ein, status, departureField, arrivalField, distance, scheduled_departure, scheduled_arrival, passengers, crew,aircraft) VALUES ({0}, '{1}', '{2}','{3}',{4}, '{5}', '{6}','Foreign key passengers', 'fk crew', 'fk aircraft')""".format((random.randint(0,9999)),str(random.choice(status)), fake.airport_icao(),fake.airport_icao(),  random.randint(0,9999),str(fake.past_datetime()), str(fake.past_datetime()))
        cursor.execute(query)
        connection.commit()
        cursorFetch = cursor.execute("SELECT * FROM scheduled_flights ORDER BY id DESC;")
        lastRec = cursorFetch.fetchone()
        print(lastRec)
        time.sleep(3)

if(__name__=="__main__"):
    main()
