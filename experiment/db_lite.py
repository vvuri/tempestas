import os
import sqlite3

DB_PATH = "./"

connection = sqlite3.connect(database=os.path.join(DB_PATH, "experiment.db"))

# Create DB
with open(os.path.join(DB_PATH, "0000-createdb.sql")) as sql_script:
    sql_statement = sql_script.read()

    cursor = connection.cursor()
    cursor.executescript(sql_statement)

    # Commit our changes
    connection.commit()

# Insert one
cursor = connection.cursor()
cursor.execute("INSERT INTO users (name, password) VALUES ('Yuri', '1234');")
cursor.close()


# Simple select
cursor = connection.cursor()
cursor.execute("SELECT id, name FROM users;")
result = cursor.fetchall()
print(result)
cursor.close()

connection.close()

# IDE
# 1) sqlite-tools-win32-x86 - https://www.sqlite.org/download.html
# 2) SQLite Studio - https://sqlitestudio.pl/
# 3) DB Browser for SQLite (DB4S) - https://sqlitebrowser.org/
