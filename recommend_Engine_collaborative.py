import psycopg2



c = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="janneke", port="2020")
cursor = c.cursor()
cursor.execute( "SELECT prodid FROM profiles_previously_viewed;" )
IDlist = []
gelijkeniscursor = c.cursor()
productnaamcursor = c.cursor()
Gelijkdic = {}
RecommendProddic = {}

def IDtolist(): #alle bekeken product ID's
    for ID in cursor.fetchall() :
        if ID != None:
            IDlist.append(ID)
        IDlist.sort()
    return IDlist


def RelatieIDmaker():
    hoeveelheid = 0
    for x in IDlist:
        Gelijklist = []
        if IDlist[IDlist.index(x)+1] == x:
            gelijkeniscursor.execute("SELECT profid FROM profiles_previously_viewed  WHERE prodid='" + str(x) + "';")
            for GelijkID in gelijkeniscursor.fetchall():
                Gelijklist.append(GelijkID)
            for y in Gelijklist:
                if Gelijklist.index(y) == 0:
                    Key = y
                else:
                    hoeveelheid += 1
                    Gelijkdic[str(hoeveelheid) + "."+ str(Key)] = str(y)

def productenvangelijken(Gelijkdic):
    hoeveelheid = 0
    for KeyID in Gelijkdic:
        for GelijkID in Gelijkdic.values():
            if KeyID.values() == GelijkID:
                cursor.execute("SELECT prodid FROM profiles_previously_viewed WHERE profid=" + str(GelijkID) + " ;")
            for prodid in gelijkeniscursor.fetchall():
                productnaamcursor.execute("SELECT name FROM products WHERE id=" + str(prodid) + " ;")
                for productnaam in gelijkeniscursor.fetchall():
                    hoeveelheid += 1
                    RecommendProddic[str(hoeveelheid) + "."+ str(KeyID)] = str(productnaam)

IDtolist()
RelatieIDmaker()
productenvangelijken(Gelijkdic)