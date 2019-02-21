# Import MySQL Connector Driver
import mysql.connector

# Import Credentials (so we can gitignore them!)
import dbcreds as dc

# Create the database if it does not exist
try:
  mydb = mysql.connector.connect(host=dc.db_host, user=dc.db_user, passwd=dc.db_pass)
  mycursor = mydb.cursor()
  mycursor.execute("create database " + dc.db_name)
except:
  print("Database already exists. Not recreating it.")

# Connect to the Database
mydb = mysql.connector.connect(host=dc.db_host, database=dc.db_name, user=dc.db_user, passwd=dc.db_pass)

# The cursor: an iterator to DB queries
mycursor = mydb.cursor()

# CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
mycursor.execute("drop table if exists users")

# Create a users table (only name and superpower)
try:
  mycursor.execute("""
    CREATE TABLE users (
      id integer AUTO_INCREMENT PRIMARY KEY,
      name       VARCHAR(30) NOT NULL,
      superpower VARCHAR(30) NOT NULL
    );
  """)
except:
  print("Table already exists. Not recreating it.")

# Insert records
query = "insert into users (name, superpower) values (%s, %s)"
values = [
  ('Rick Gessner','C+++++'),
  ('Manjot Bilkhu','Teleportation'),
  ('Raul Pegan','Bolockschain'),
  ('Ramsin Khoshabeh','Scooting in the Rain')
]
mycursor.executemany(query, values)
mydb.commit()

print('---------- DATABASE INITIALIZED ----------')