'''
kaylin lee
sprint 2
random entry into airline
'''

# libraries
import sqlite3
import time
import random
from faker import Faker
from faker_airtravel import AirTravelProvider

# airline
# ein (INT), airline name (TEXT)

def main():
    fake = Faker()
    fake.add_provider(AirTravelProvider)

    # test print 5 times
    for i in range(1,5):

        values = [str("%05d" % random.randint(0,999999999)), "'" + fake.airline()+ "'"]
        query = f"INSERT INTO airlines (ein, name) VALUES (" + ','.join(values) + ")"
        # print test query
        print(query)
        # every 3 minutes
        time.sleep(5)

if (__name__=="__main__"):
    main()
