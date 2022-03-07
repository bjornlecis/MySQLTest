import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd ="root",
  database ="testdatabase"
)

mycursor = db.cursor()

def voeg_persoon_toe():
    naam = input("geef de naam in")
    leeftijd = input("geef leeftijd in")
    mycursor.execute("INSERT INTO Person(name,age) VALUES (%s,%s)",(naam,leeftijd))
    db.commit()


def toon_personen_naam():
    mycursor.execute("SELECT * FROM Person")
    for x in mycursor:
      print(x)

def verwijder_persoon():
    naam = input("geef de naam van persoon in")
    sqlstring = "DELETE FROM Person WHERE name = "+"'"+naam+"'"
    mycursor.execute(sqlstring)
    db.commit()

def wijzig_naam():
    oude_naam = input("geef de naam van persoon in")
    nieuwe_naam = input("geef de nieuwe naam van de persoon in")
    sqlstring ="UPDATE Person SET name = "+"'"+nieuwe_naam+"'" + "WHERE name = "+"'"+oude_naam+"'"
    mycursor.execute(sqlstring)
    db.commit()

def wijzig_leeftijd():
    naam = input("geef de naam van persoon in")
    nieuwe_leeftijd = input("geef de nieuwe leeftijd van de persoon in")
    if nieuwe_leeftijd.isnumeric():
        sqlstring ="UPDATE Person SET age = "+"'"+nieuwe_leeftijd+"'" + "WHERE name = "+"'"+naam+"'"
        mycursor.execute(sqlstring)
        db.commit()
    else:
        print("Kan niet wijzigen")

def keuzes():
    print("1: toon personen")
    print("2: voeg persoon toe")
    print("3: verwijder persoon")
    print("4: wijzig naam")
    print("5: wijzig leeftijd")

keuzes()
keuze = input("geef je keuze in")
while(not keuze == "stop"):
    if keuze == "1":
        toon_personen_naam()
    elif keuze == "2":
        voeg_persoon_toe()
    elif keuze == "3":
        verwijder_persoon()
    elif keuze == "4":
        wijzig_naam()
    else:
        wijzig_leeftijd()
    keuzes()
    keuze = input("geef je keuze in")
