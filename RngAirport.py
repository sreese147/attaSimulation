#Vivek DID This.
# Import string and random module
import string
import random
import sys
from faker import Faker
fake = Faker()
def RanIcao():

    # Randomly choose a letter from all the ascii_uppercase
    rL1 = random.choice(string.ascii_uppercase)
    rL2 = random.choice(string.ascii_uppercase)
    rL3 = random.choice(string.ascii_uppercase)
    rL4 = random.choice(string.ascii_uppercase)
    rLt = rL1+rL2+rL3+rL4
    List1 = [rLt]




def generate_iata_code():
    """
    Generates a random 3-letter IATA code.
    """
    iata_code = ''.join(random.choices(string.ascii_uppercase, k=3))



VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))


def generate_word(length):
    word = ""
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)




def lat_decimal():
    Lat = random.randint(-90.0, 90.0)


def lon_decimal():
    Lon = random.randint(-180.0,180.0)


def fake_country():
    fake.country()

def fake_name():
    fake.name()
def fake_city():
    fake.city()



def results():
    results = [RanIcao() for x in range(10)]
    results2 = [generate_iata_code() for x in range(10)]
    results3 = [generate_word(11) for x in range(10)]
    results4 = [lat_decimal() for x in range(10)]
    resluts5 = [lon_decimal() for x in range(10)]
    results6 = [fake_country() for x in range(10)]
    results7 = [fake_name() for x in range(10)]
    results7 = [fake_city() for x in range(10)]


def main():
    results()








if(__name__=="__main__"):
    main()
