import psycopg2, random, json



def get_cursor():
    cur = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="janneke", port="2020").cursor()
    return cur


def get_all_items():
    cur = get_cursor()
    cur.execute("SELECT id, brand, subsubcategory FROM products WHERE brand IS NOT NULL; ")
    Allproductslist = cur.fetchall()
    random.shuffle(Allproductslist) #met dank aan Adam's slimme manier van kansgeving
    return Allproductslist

def get_all_profiles():
    cur = get_cursor()
    cur.execute("SELECT profid, prodid FROM profiles_previously_viewed; ")
    Allprofileslist = cur.fetchall()
    random.shuffle(Allprofileslist)  # so every products has a chance to be recommended
    return Allprofileslist


def get_similar(List):
    similaritemlist = []
    amountofvalues = len(List[0])
    for All_items in List:
        comparelist = List
        comparelist.remove(All_items)
        similar_items_id = [All_items[0]]
        for comparing_item in comparelist:
            if amountofvalues == 2:
                if All_items[1] == comparing_item[1]:
                    similar_items_id.append(comparing_item[0])
                    if len(similar_items_id) > 3:
                        similaritemlist.append(similar_items_id)
                        break
            if amountofvalues == 3:
                if All_items[1] == comparing_item[1] and All_items[2] == comparing_item[2]:
                    similar_items_id.append(comparing_item[0])
                    if len(similar_items_id) > 3:
                        similaritemlist.append(similar_items_id)
                        break
    return similaritemlist

def csvfilewriter(similarlist):
    with open("Datarelatieproducts.csv", "w") as outfile:
        json.dump(similarlist, outfile)

def csvfileadder(similarlist):
    with open("Datarelatieproducts.csv", "a+") as outfile:
        json.dump(similarlist, outfile)

def contentfiltering():
    Allproductslist = get_all_items()
    similar_items = get_similar(Allproductslist)
    csvfilewriter(similar_items)
    print("contentfiltering results: " + str(similar_items))

def collaberativefiltering():
    Allprofileslist = get_all_profiles()  # gives all products in a list
    similar_items = get_similar(Allprofileslist)  # gives similar profiles as ID in a list
    csvfileadder(similar_items)
    print("collaberativefiltering results: " + str(similar_items))


contentfiltering()
collaberativefiltering()
