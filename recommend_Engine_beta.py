import psycopg2, os, sys, time, json

c = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="janneke", port="2020")
cursor = c.cursor()
cursor.execute( "SELECT name FROM products;" )
relatiecursor = c.cursor()
namecursor = c.cursor()
namelist = []
relatiedictionary = {}
x = 0


def nametolist():
    for name in cursor.fetchall() :
        name = name[-1]
        if name != None:
            namelist.append(name)
    return namelist

def relatielijstmaker(namelist, relatiedictionary, x):
    # for name in namelist:
        name = namelist[1]
    # for relatie in namelist: #mogelijke relatie tussen product
        relatie = namelist[3]
        if x < 1:
            laadpunt = "category"
            sys.stdout.write('\r' + 'Naam nummer ' + str(namelist.index(name) + 1) + " laden en " + laadpunt + ' Relatie nummer ' + str(namelist.index(relatie) + 1) + " laden \n")
            x = categorychecker(name, relatie)
        # for relatie in namelist:
        #     laadpunt = "sub-category"
        #     sys.stdout.write('\r' + 'Naam nummer ' + str(namelist.index(name) + 1) + " laden en " + laadpunt + ' Relatie nummer ' + str(namelist.index(relatie) + 1) + " laden")
        #     subcategorychecker(name, relatie)


# def subcategorychecker(name, relatie):
#     relatiecursor.execute("SELECT subcategory FROM products;")
#     namecursor.execute("SELECT subcategory FROM products WHERE name='" + str(name) + "';")
#     namesubcategory = namecursor.fetchall()
#     for relatiesubcategory in relatiecursor.fetchall():
#         if relatiesubcategory ==  namesubcategory:
#             relatiedictionary[name] = relatie

def categorychecker(name, relatie):
    global x
    relatiecursor.execute("SELECT category FROM products;")
    namecursor.execute("SELECT category FROM products WHERE name='" + str(name) + "';")
    namecategory = namecursor.fetchall()
    namecategory = namecategory[-1]
    print("name:" + str(namecategory))
    for relatiecategory in relatiecursor.fetchall():
        print(relatiecategory)
        # print("name: " + str(namecategory))
        # print("relatie: " + str(relatiecategory))
        if relatiecategory ==  namecategory:
            print("correct")
            print("relatie:"+ str(relatie))
            x += 1
            relatiedictionary[str(x) + ". " + name] = relatie
        elif x != 0:
            x = x
        else:
            x = 0
    return x







nametolist()
relatielijstmaker(namelist, relatiedictionary, x)
with open ("Datarelatiedict.json", "w") as outfile:
    json.dump(relatiedictionary, outfile)
print(relatiedictionary)