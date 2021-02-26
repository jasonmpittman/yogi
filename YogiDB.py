import sqlite3


connection = sqlite3.connect('Yogi_Database.db') # Creates the databse called Yogi_Databse.

cursor = connection.cursor()

# Creates port table which contains on attribute called port_ID which is the primary key of the table.

table1 = """CREATE TABLE IF NOT EXISTS
port(port_ID INTEGER PRIMARY KEY)"""


# Creates fingerprint table which contains multiple atributes: fingerprint_ID = primary key, OS, Packets_S, 
# IP_addr, Firewall_status, and Packets_R.

table2 = """CREATE TABLE IF NOT EXISTS
Fingerprint(Fingerprint_ID INTEGER PRIMARY KEY, OS STRING, Packets_S FILE, IP_addr STRING, Firewwall_Status STRING,
Packets_R File)"""



    









if __name__ == '__main__':

