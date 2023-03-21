"""Sabrina Reese + Rose Coluzzi
Cmdr Schenk
sprint 2
scheduled flight
period 5 cs50 ap"""
import time
import random
from faker import Faker
from faker_airtravel import AirTravelProvider
import sqlite3
import mysql.connector

#Rose Coluzzi 
from TableControllers.FlightTable import FlightTable
from TableControllers.AirlineTable import AirlineTable
from TableControllers.PassengerTable import PassengerTable
from TableControllers.CrewTable import CrewTable
from TableControllers.ScheduledFlightTable import ScheduledFlightTable
# Utilities
from TableOptions import TableOptions 


def main():

    #Sabrina Reese
    #Set the faker library to variable fake
    #and get the air travel section of the faker library
    fake = Faker()
    fake.add_provider(AirTravelProvider)
    
    status= ["Awaiting", "Boarding", "Departing", "InFlight - OnTime", "InFlight - Late", "Landed - On Time", "Landed - Late", "Cancelled", "Delayed", "Unknown"]
    
    #Rose Coluzzi 
    passengerX = passengerDB.read()
    crewX = crewDB.read()
    aircraftX = aircraftDB.read()
    
    for i in range(1,5):
        #Sabrina Reese
        #insert sql rec
        query = """INSERT INTO scheduled_flights (ein, status, departureField, arrivalField, distance, scheduled_departure, scheduled_arrival, passengers, crew,aircraft) VALUES ({0}, '{1}', '{2}','{3}',{4}, '{5}', '{6}','Foreign key passengers', 'fk crew', 'fk aircraft')""".format((random.randint(0,9999)),str(random.choice(status)), fake.airport_icao(),fake.airport_icao(),  random.randint(0,9999),str(fake.past_datetime()), str(fake.past_datetime()))
        cursor.execute(query)
        connection.commit()
        cursorFetch = cursor.execute("SELECT * FROM scheduled_flights ORDER BY id DESC;")
        rec = cursorFetch.fetchone()
        print(rec)
        #repeat every 3 min (3 sec)
        time.sleep(3)

if(__name__=="__main__"):
    main()
