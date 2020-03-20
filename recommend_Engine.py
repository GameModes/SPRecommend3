import psycopg2, sys, json, os
from progress.bar import Bar

c = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="janneke", port="2020")
cursor = c.cursor()
cursor.execute( "SELECT name FROM products;" )
relatiecursor = c.cursor() #de relatiezoeker
namecursor = c.cursor() #de naamzoeker
namelist = []
relatiedictionary = {} #de dictionary waar alle relaties staan

def nametolist():
    for name in cursor.fetchall() :
        name = name[-1]
        if name != None:
            namelist.append(name)
    return namelist

def relatiedicmaker (namelist, relatiedictionary):
    for name in namelist:
        relatielist = namelist #om ervoor te zorgen dat dezelfde product geen relatie wordt
        relatielist.remove(name)
        for relatie in relatielist:
            if len(relatiedictionary) < 5: #het product krijgt maximaal 4 relaties
                laadpunt = "category" #defineert wat de lader laad
                sys.stdout.write('\r' + laadpunt + ' Relatie nummer ' + str(relatielist.index(relatie) + 1)+ "/"+ str(len(relatielist)) + " laden \n")
                #categorychecker
                relatiecursor.execute("SELECT category FROM products;")
                namecursor.execute("SELECT category FROM products WHERE name='" + str(name) + "';")
                namecategory = namecursor.fetchall()
                namecategory = namecategory[-1]
                for relatiecategory in relatiecursor.fetchall():
                    if relatiecategory ==  namecategory:
                        for nummer in range (1,4):
                            relatiedictionary[str(nummer) + ". " + name] = relatie



def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

nametolist()
relatiedicmaker (namelist, relatiedictionary)
with open ("Datarelatiedict.json", "w") as outfile:
    json.dump(relatiedictionary, outfile)
print(relatiedictionary)
