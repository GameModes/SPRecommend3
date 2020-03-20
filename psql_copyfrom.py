
import psycopg2

c = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="janneke", port="2020")
cursor = c.cursor()
cursor.execute( "SELECT name FROM products" )
for name in cursor.fetchall() :
    if
         print (name)

# cur = c.cursor()
#
# filenames = ['products', 'profiles', 'profiles_previously_viewed', 'sessions']
#
# for filename in filenames:
#     with open(filename+'.csv') as csvfile:
#         print("Copying {}...".format(filename))
#         cur.copy_expert("COPY "+filename+" FROM STDIN DELIMITER ',' CSV HEADER", csvfile)
#         c.commit()
#
# c.commit()
# cur.close()
# c.close()

# hostname = 'localhost'
# username = 'postgres'
# password = 'janneke'
# database = 'postgres'
#
# # Simple routine to run a query on a database and print the results:
# def doQuery( conn ) :
#     cur = conn.cursor()
#
#     cur.execute( "SELECT name FROM products" )
#
#     for firstname, lastname in cur.fetchall() :
#         print (firstname, lastname)
#
#
# print ("Using psycopg2…")
# import psycopg2
# myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
# doQuery( myConnection )
# myConnection.close()
#
# print ("Using PyGreSQL…")
# import pgdb
# myConnection = pgdb.connect( host=hostname, user=username, password=password, database=database )
# doQuery( myConnection )
# myConnection.close()