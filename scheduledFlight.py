"""Sabrina Reese
Cmdr Schenk
Feb 9 2023
progress check 1
scheduled flight
period 5 cs50 ap"""
import time
import random
from faker import Faker
from faker_airtravel import AirTravelProvider


def main():

    fake = Faker()
    fake.add_provider(AirTravelProvider)


    status = ["Awaiting", "Boarding", "Departing", "InFlight -- OnTime", "InFlight -- Late", "Landed - On Time", "Landed - Late", "Cancelled", "Delayed", "Unknown"]
    values = [ str(random.randint(0,9999)), str(random.randint(0,9999)), random.choice(status), fake.airport_icao(), fake.airport_icao(), str(random.randint(0,9999)), str(fake.past_datetime()), str(fake.past_datetime()), 'Foreign key passengers', 'foreign key crew', 'foreign key aircraft ' ]

    query = f"INSERT INTO scheduledFlight () VALUES ()" + ','.join(values)

    print(query)

if(__name__=="__main__"):
    main()
