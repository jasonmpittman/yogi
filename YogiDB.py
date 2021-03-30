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

# Creates honeypot_characteristics table. This is a linking table making a one to many relationship with Fingerprint and Por.
# The primary keys for Port and Fingerprint will be used as both foreign keys and as a composite primary key.

table3 = """CREATE TABLE IF NOT EXISTS
Honeypot_Characteristics(Fingerprint_ID INTEGER PRIMARY KEY FOREIGN KEY, Port_ID INTEGER PRIMARY KEY FOREIGN KEY)
"""

def create_connection(Yogi_Database.db):
    """ create databse connection to the SQLite databse
    specified by the db_file
    : param db_file: databse file
    : return: Connection object or None
    """

    conn = None

    try:
        conn = sqlite3.connect(Yogi_Database.db)

    except Error as e:
        print(e)


    return conn







if __name__ == '__main__':

