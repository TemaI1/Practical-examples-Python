import sqlite3

db = sqlite3.connect('server.sqlite')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    age INT,
    placement TEXT,
    telephone BIGINT
)""")
db.commit()