import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd ="root",
  database ="voertuigen"
)

class Voertuig:
  def __init__(self,id,merk,model,bouwjaar,brandstof,verhuurd):
    self.id = id
    self.merk = merk
    self.model = model
    self.bouwjaar = bouwjaar
    self.brandstof = brandstof
  def __str__(self):
    return "merk en model: {} {}\nbouwjaar: {} ".format(self.merk,self.model,self.bouwjaar)

mycursor = db.cursor()
lijst_autos = []

def toon_voertuigen():
    mycursor.execute("SELECT * FROM auto")
    for x in mycursor:
      lijst_autos.append(Voertuig(x[0],x[1],x[2],x[3],x[4],x[5]))

def toon_lijst_autos():
    for x in lijst_autos:
      print(x)

def toon_voertuigen_niet_verhuurd():
  mycursor.execute("SELECT * FROM auto WHERE Verhuurd = 'Nee'")
  for x in mycursor:
      print(*x)

def voeg_auto_toe():
    merk = input("geef het merk in")
    model = input("geef het model in")
    bouwjaar = input("geef het bouwjaar in")
    brandstof = input("geef brandstof in")
    verhuurd = input("wagen verhuurd ja of nee")
    mycursor.execute("INSERT INTO auto(merk,model,bouwjaar,brandstof,verhuurd) VALUES (%s,%s,%s,%s,%s)"
    ,(merk,model,bouwjaar,brandstof,verhuurd))
    db.commit()

def huur_auto():
    print("deze wagens zijn nog beschikbaar")
    toon_voertuigen_niet_verhuurd()
    id = input("geef het id van de wagen die je wenst te huren")
    sqlstring ="UPDATE auto SET Verhuurd = 'Ja'" + "WHERE idAuto = "+"'"+id+"'"
    mycursor.execute(sqlstring)
    db.commit()

def verwijder_auto():
  toon_lijst_autos()
  id = input("Geef het id van de wagen dat je wenst te verwijderen")
  sqlstring = "DELETE FROM auto WHERE idAuto = "+"'"+id+"'"
  mycursor.execute(sqlstring)
  db.commit()


toon_voertuigen()
verwijder_auto()
toon_voertuigen()
