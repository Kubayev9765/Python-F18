1.
  with sqlite3.connect("Roster.db") as connection:
    cursor= connection.cursor()
    query=" create table Roster(Name text, Species text, Age int)"
    cursor.execute(query)
2.

import sqlite3
values=(
    ('Benjamin Sisko', 'Humon',40),
    ('Jadzia Dax','Trill', 300),
    ('Kira Nerys', 'Bajoron', 29)
)
with sqlite3.connect("Roster.db") as connection:
    cursor= connection.cursor()
    query=("INSERT INTO Roster VALUES(?, ?, ?)", values)    
    cursor.executemany(query)
    query=("""
      UPDATE Roster
      SET Name = 'Ezri Dax'
      WHERE Name = 'Jadzia Dax'  
    """);
      cursor.executescript(query)
      query=("""
                SELECT Name, Age
                FROM Roster
                WHERE Species = 'Bajoran'      
      """);
      cursor.executescript(query)
      

