import random
from faker import Faker

# Create a Faker object to generate fake data
fake = Faker()

# Define the schema for the table
schema = {
    "id": "text",
    "first_name": "text",
    "last_name": "text",
    "qualifactions": "enum: Captain, FirstOfficer, JuniorFA, SeniorFA, FlightEngineer",
    "plane_qualifications": "enum: 737, 777, L1011",
    "crew": "int"
}

# Generate a random SQL query to insert data into the table
query = f"INSERT INTO passengers ({','.join(schema.keys())}) VALUES ()"
values = [f"'{fake.uuid4()}'", f"'{fake.first_name()}'", f"'{fake.last_name()}'", f"'{random.choice(['Captain', 'FirstOfficer', 'JuniorFA', 'SeniorFA', 'FlightEngineer'])}'", f"'{random.choice(['737', '777', 'L1011'])}', 'PUT FOREIGN KEY HERE')"]
query += ','.join(values)

print(query)