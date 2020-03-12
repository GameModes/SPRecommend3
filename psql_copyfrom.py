import psycopg2

c = psycopg2.connect("dbname=postgres user=postgres password=postgres")  #TODO: edit this.
cur = c.cursor()

filenames = ['products', 'profiles', 'profiles_previously_viewed', 'sessions']

for filename in filenames:
    with open(filename+'.csv') as csvfile:
        print("Copying {}...".format(filename))
        cur.copy_expert("COPY "+filename+" FROM STDIN DELIMITER ',' CSV HEADER", csvfile)
        c.commit()

c.commit()
cur.close()
c.close()