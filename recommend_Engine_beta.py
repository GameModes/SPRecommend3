import psycopg2, os

c = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="janneke", port="2020")
cursor = c.cursor()
cursor.execute( "SELECT name FROM products;" )
relatiecursor = c.cursor()
namecursor = c.cursor()
namelist = []
relatiedictionary = {}


def nametolist():
    for name in cursor.fetchall() :
        name = name[-1]
        if name != None:
            namelist.append(name)
    return namelist

def relatielijstmaker(namelist, relatiedictionary):
    for name in namelist:
        for relatie in namelist: #mogelijke relatie tussen product
            print('Naam ' + str(namelist.index(name) + 1) + " laden")
            print('Relatie ' + str(namelist.index(relatie) + 1) + " laden")
            os.system('cls' if os.name == 'nt' else 'clear')
            subcategorychecker(name, relatie)



def subcategorychecker(name, relatie):
    relatiecursor.execute("SELECT subcategory FROM products;")
    namecursor.execute("SELECT subcategory FROM products WHERE name='" + str(name) + "';")
    namesubcategory = namecursor.fetchall()
    for relatiesubcategory in relatiecursor.fetchall():
        if relatiesubcategory ==  namesubcategory:
            relatiedictionary[name] = relatie




nametolist()
relatielijstmaker(namelist, relatiedictionary)
print(relatiedictionary)