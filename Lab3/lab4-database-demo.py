import sqlite3

connect = sqlite3.connect('sensors.db')
connect.row_factory = sqlite3.Row
cursor = connect.cursor()

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
print("\nSensors")
for row in cursor:
    print(row['sensorID'],row['type'], row['zone']);
print("\nSensors in kitchen")
#Print sensors in kitchen
cursor.execute("SELECT * FROM sensor WHERE zone = 'kitchen'")
for row in cursor:
    print(row['sensorID'],row['type'], row['zone']);
#Print Door sensors
print("\nDoor sensors")
cursor.execute("SELECT * FROM sensor WHERE type = 'door'") 
for row in cursor:
        print(row['sensorID'],row['type'], row['zone']);
print("\n")

#Drop table for testing and aesthetics, items don't repeat every execution
cursor.execute("DROP TABLE sensor")
connect.close();
