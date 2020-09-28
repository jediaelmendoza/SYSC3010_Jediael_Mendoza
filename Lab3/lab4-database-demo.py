import sqlite3

connect = sqlite3.connect('sensors.db')
connect.row_factory = sqlite3.Row
cursor = connect.cursor();

#Create Table
cursor.execute("CREATE TABLE IF NOT EXISTS sensor(sensorID INTEGER, type TEXT, zone TEXT)")

#Add items
cursor.execute("INSERT INTO sensor VALUES(1,'door','kitchen')")
cursor.execute("INSERT INTO sensor VALUES(2,'temperature','kitchen')")
cursor.execute("INSERT INTO sensor VALUES(3,'door','garage')")
cursor.execute("INSERT INTO sensor VALUES(4,'motion','garage')")
cursor.execute("INSERT INTO sensor VALUES(5,'temperature','garage')")
connect.commit();

#Print
cursor.execute("SELECT * FROM sensor");

for row in cursor:
    print(row['sensorID'],row['type'], row['zone']);
    
#Reset the table just for aesthetics and testing so that data won't repeat 
cursor.execute("DROP TABLE sensor")

connect.close();
