import mysql.connector

class Persoon:
    def __init__(self,naam,leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd
    def __str__(self):
        return "De persoon heet {} en is {} jaar oud".format(self.naam,self.leeftijd)


lijst_personen = []


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
      lijst_personen.append(Persoon(x[0],x[1]))

def toon_lijst_personen():
    for x in lijst_personen:
        print(x)
    print(len(lijst_personen))

#voeg_persoon_toe("Dennis",25)
#voeg_persoon_toe("Mark",42)

toon_personen_naam()
toon_lijst_personen()

