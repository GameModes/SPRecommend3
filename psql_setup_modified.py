import psycopg2

c = psycopg2.connect("dbname=SPRecommendop3  user=postgres password=") #TODO: edit this.
cur = c.cursor()

cur.execute("DROP TABLE IF EXISTS products CASCADE")
cur.execute("DROP TABLE IF EXISTS profiles CASCADE")
cur.execute("DROP TABLE IF EXISTS profiles_previously_viewed CASCADE")
cur.execute("DROP TABLE IF EXISTS sessions CASCADE")

# All product-related tables

cur.execute("""CREATE TABLE products
                (id VARCHAR PRIMARY KEY,
                 name VARCHAR,
                 brand VARCHAR,
                 type VARCHAR,
                 category VARCHAR,
                 subcategory VARCHAR,
                 subsubcategory VARCHAR,
                 targetaudience VARCHAR,
                 msrp INTEGER,
                 discount INTEGER,
                 sellingprice INTEGER,
                 deal VARCHAR,
                 description VARCHAR);""")

# All profile-related tables

cur.execute("""CREATE TABLE profiles
                (id VARCHAR PRIMARY KEY,
                 latestactivity TIMESTAMP,
                 segment VARCHAR);""")

cur.execute("""CREATE TABLE profiles_previously_viewed
                (profid VARCHAR,
                 prodid VARCHAR,
                 FOREIGN KEY (profid) REFERENCES profiles (id),
                 FOREIGN KEY (prodid) REFERENCES products (id));""")

# All session-related tables

cur.execute("""CREATE TYPE d_type AS ENUM ('mobile', 'tablet', 'pc', 'other');""")
cur.execute("""CREATE TABLE sessions
                (id VARCHAR PRIMARY KEY,
                 profid VARCHAR,
                 segment VARCHAR,
                 sale BOOLEAN,
                 starttime TIMESTAMP,
                 endtime TIMESTAMP,
                 duration INTEGER,
                 os VARCHAR,
                 devicefamily VARCHAR,
                 devicetype d_type,
                 FOREIGN KEY (profid) REFERENCES profiles (id));""")

c.commit()
cur.close()
c.close()