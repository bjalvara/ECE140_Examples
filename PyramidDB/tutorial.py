# Import MySQL Connector Driver
import mysql.connector

# Credentials (STORE THESE SECURELY!)
db_user = "root"
db_pass = "root"
db_name = "ece140a"
db_host = "localhost"

# Connect to the Database
mydb = mysql.connector.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
# or if the DB does not exist yet...
# mydb = mysql.connector.connect(host=db_host, user=db_user, passwd=db_pass)
print(mydb)

mycursor = mydb.cursor()
# # Create a database if it does not exist
# try:
#   mycursor.execute("create database " + db_name)
# except:
#   print("Database already exists. Not recreating it.")

# Show all databases
mycursor.execute("show databases")
print('---------- DATABASES ----------')
[print(x) for x in mycursor]

# # CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!! CAUTION!!!
mycursor.execute("drop table if exists Users")

# Create a Users table
try:
  mycursor.execute("""
    CREATE TABLE Users (
      id integer AUTO_INCREMENT PRIMARY KEY,
      first_name VARCHAR(30) NOT NULL,
      last_name  VARCHAR(30) NOT NULL,
      email      VARCHAR(50) NOT NULL,
      age        int,
      created_at TIMESTAMP
    );
  """)
except:
  print("Table already exists. Not recreating it.")

# Show all tables
mycursor.execute("show tables")
print('---------- TABLES ----------')
[print(x) for x in mycursor]

# Describe Users Table
mycursor.execute("describe Users")
print('---------- USERS TABLE ----------')
[print(x) for x in mycursor]

# Insert Multiple Records
query = "insert into Users (first_name, last_name, email, age) values (%s, %s, %s, %s)"
values = [
  ('Bill','Gates','bill@gates.com', 65),
  ('Elon','Musk','elon@mask.com', 45)
]
mycursor.executemany(query, values)
mydb.commit()
print('---------- INSERT ----------')
print(mycursor.rowcount, "record(s) inserted.")

# Updating Records
mycursor.execute("update Users set email='elon@must.com' where id=2;")
mydb.commit()
print('---------- UPDATE ----------')
print(mycursor.rowcount, "record(s) updated.")

# Deleting Records
mycursor.execute("delete from Users where last_name = 'Musk'")
mydb.commit()
print('---------- DELETE ----------')
print(mycursor.rowcount, "record(s) deleted.")

# Selecting Records
mycursor.execute("select * from Users;")
myresult = mycursor.fetchall()
print('---------- SELECT ----------')
[print(x) for x in myresult]