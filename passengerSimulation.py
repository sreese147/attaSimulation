'''
Dylan Torres-Tejada
AP Comp Sci 50
Cmdr Schenk

RNG Simulation
Passengers
'''

#Preprocessor Directives

from faker import Faker
#Note: The Faker library was demonstrated to me by Lance; thank you.
import random as rr
import random
from time import time
import sqlite3

#Note on faker: The Faker library provides fake names and text depending on the type of text requested. Examples shown below


#----------------------------------------------------------------------------------------------------------------------------#

class PSim():
  def createConn(self):
    self.connection = sqlite3.connect("Pas1.db")
    self.cursor = self.connection.cursor()
  
  def breakConn(self):
    self.connection.close()
    self.cursor.close()
  
  def __init__(self):
    #Connection Established
    self.createConn()
    #Imported Libraries made POCO-compatible
    self.fake = Faker()
    self.random = rr.random()
    self.time = time()
    self.countries = [
        "South Africa", "United States", "Australia", "France",
        "Republic of Korea", "Pakistan", "Libya", "Brazil", "Kenya", "Albania",
        "Slovenia", "Spain", "Benin", "Greece", "Italy", "Colombia",
        "United Kingdom", "Ukraine", "Afghanistan", "Russia",
        "Bosnia and Herzegovina", "Namibia", "Mexico", "Switzerland", "Serbia",
        "Peru", "Morocco", "Azerbaijan", "Estonia", "Germany", "India",
        "Reunion", "Iceland", "Israel", "Jamaica", "Malta", "Japan", "Kiribati",
        "Malawi", "Macao", "Egypt", "Seychelles", "Papua New Guinea",
        "United Arab Emirates", "Canada", "Latvia", "New Zealand", "Portugal",
        "S.A.", "Argentina", "ALASKA", "Tanzania", "Burkina Faso", "Austria",
        "Ecuador", "AVIANCA", "Vanuatu", "Bangladesh", "Netherlands", "Malaysia",
        "Bolivia", "Zimbabwe", "Venezuela", "Ivory Coast", "Botswana",
        "French Polynesia", "Bulgaria", "Togo", "Russian Federation", "China",
        "Marshall Islands", "Algeria", "Indonesia", "Ireland", "Finland", "Fiji",
        "Faroe Islands", "Philippines", "Guinea", "Denmark", "French Guiana",
        "Myanmar", "Turkey", "Democratic People's Republic of Korea",
        "Kazakhstan", "Armenia", "Mauritius", "Madagascar", "Moldova", "Nigeria",
        "Sri Lanka", "Sierra Leone", "Republic of the Congo", "Uzbekistan",
        "Bahamas", "Thailand", "Hungary", "Belarus", "Belgium", "Romania",
        "Sweden", "Trinidad and Tobago", "Iran", "Hong Kong SAR of China",
        "Cayman Islands", "Czech Republic", "Poland", "Taiwan", "Burundi",
        "Kyrgyzstan", "Comoros", "Panama", "Croatia", "Cuba", "Cyprus",
        "Djibouti", "Dominican Republic", "DRAGON", "Bhutan",
        "Netherlands Antilles", "Uganda", "Eritrea", "Ethiopia", "Lithuania",
        "Georgia", "Ghana", "Costa Rica", "Oman", "Bahrain", "Haiti", "Iraq",
        "Honduras", "Kuwait", "Singapore", "Chile",
        "Lao Peoples Democratic Republic", "Antigua and Barbuda", "Mozambique",
        "Norway", "Luxembourg", "Macedonia", "Mongolia", "Belize", "Lebanon",
        "Montenegro", "Nauru", "Nepal", "Tunisia", "Saudi Arabia", "Hong Kong",
        "Mauritania", "Uruguay", "Cambodia", "Vietnam", "Samoa", "Qatar",
        "Cook Islands", "Brunei", "Jordan", "Rwanda", "Sudan",
        "Syrian Arab Republic", "Slovakia", "Suriname", "Solomon Islands",
        "Tajikistan", "Aruba", "Turkmenistan", "Angola", "Paraguay", "Yemen",
        "\\N", "Maldives", "Burma", "Gabon", "South Korea",
        "Saint Vincent and the Grenadines", "Guadeloupe", "Equatorial Guinea",
        "Cape Verde", "Congo (Kinshasa)", "Zambia", "Cameroon", "Niger",
        "Sao Tome and Principe", "Palau", "Syria", "American Samoa", "Barbados",
        "British Virgin Islands", "Senegal", "Puerto Rico", "Tonga",
        "South Sudan"
    ]
    #The List above is the list of countries recognized by Atta Airlines
  
    #Lists for Random Passenger Queries
    self.listoN = ["0", "1", "2", "3", "4", "5", "6" ,"7", "8" , "9"]
    self.gender = ["M", "F"]
    self.ffStatus = ["Y", "N"]
  
    #Numbers for Frequent Flier Number (4 digits)
    self.ffnoW = random.randint(0,9999)
    #Calls function that creates queries
    self.randomPassenger(random.randint(0,9), self.ffnoW, self.fake.first_name(),self.fake.last_name(), random.choice(self.gender), random.choice(self.countries), random.choice(self.ffStatus))
  
  
  def randomPassenger(self, id, ffno, fn, ln, ge, na, nfs):
  
    #Parameters Key:
    #ffno = frequent flyer number
    #fn = first name
    #ln = last name
    #ge = gender
    #na = nationality
    #nfs = no fly status
  
    while True:
      print(id, ffno, fn, ln, ge, na, nfs)
      
      self.cursor.execute(f"INSERT INTO passenger (id,ff_no,first_name,last_name,gender,nationality, no_fly_status) VALUES ('{id}','{ffno}','{fn}','{ln}', '{ge}','{na}', '{nfs}')")
  
      '''self.lInput = input()
      if (self.lInput == 'Stop' or self.lInput == 'stop'):
        self.breakConn()
        
      else: 
        pass
        '''
      time.sleep(30)
        
  
