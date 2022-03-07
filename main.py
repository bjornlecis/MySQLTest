import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd ="root",
  database ="testdatabase"
)

mycursor = db.cursor()

def voeg_persoon_toe(naam, leeftijd):
  mycursor.execute("INSERT INTO Person(name,age) VALUES (%s,%s)",(naam,leeftijd))
  db.commit()


#mycursor.execute("CREATE TABLE Person(name VARCHAR(50),age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
def toon_personen_naam():
    mycursor.execute("SELECT * FROM Person")
    for x in mycursor:
      print(x)

#voeg_persoon_toe("Dennis",25)
#voeg_persoon_toe("Mark",42)

toon_personen_naam()


