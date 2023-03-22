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
    
    #to avoid forever loops, the program needs to be restarted every "day"
    for i in range(1,480):
        #Sabrina Reese
        time.sleep(1)
        #make sure that the departure time is before the arrival time
        #if it is not, it reassigns a new departure time
        dept = fake.past_datetime()
        arri = fake.past_datetime()
        while dept > arri:
            dept = fake.past_datetime()
        #insert sql rec
        query = """INSERT INTO scheduled_flights (ein, status, departureField, arrivalField, distance, scheduled_departure, scheduled_arrival, passengers, crew,aircraft) VALUES ({0}, '{1}', '{2}','{3}',{4}, '{5}', '{6}','{7}', '{8}', '{9}')""".format((random.randint(0,9999)),str(random.choice(status)), fake.airport_icao(),fake.airport_icao(),  random.randint(0,9999),str(dept), str(arri), str(passengerX[0][3]), str(crewX[0][3]), str(aircraftX[0][3]))
        cursor.execute(query)
        connection.commit()
        cursorFetch = cursor.execute("SELECT * FROM scheduled_flights ORDER BY id DESC;")
        rec = cursorFetch.fetchone()
        print(rec)
        #repeat every 3 min (3 sec)
        time.sleep(2)

if(__name__=="__main__"):
    main()
