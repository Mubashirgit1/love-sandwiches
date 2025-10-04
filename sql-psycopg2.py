import psycopg2

# Connect to your postgres chinook DB
Connection = psycopg2.connect(
    database="chinook",
    user="postgres",        # your PostgreSQL username
    password="mubashir", # your PostgreSQL password
    host="localhost",
    port="5432"
)

# Open a cursor to perform database operations
Cursor = Connection.cursor()

# execute a query
# Cursor.execute('SELECT * FROM "artist"')
# Cursor.execute('SELECT "name" FROM "artist"')
# Cursor.execute('SELECT * FROM "artist" WHERE "name" = %s',["Queen"])
# Cursor.execute('SELECT * FROM "artist" WHERE "artist_id" = %s',[51])
# Cursor.execute('SELECT * FROM "artist" WHERE "name" = %s OR "name" = %s',["Queen","AC/DC"])
Cursor.execute('SELECT * FROM "track"')
# fetch the results
results = Cursor.fetchall()

# fetch the result single
result = Cursor.fetchone()

# close the connection
Connection.close()

for row in results:
    print(row)
