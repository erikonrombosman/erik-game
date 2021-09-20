import sqlite3

con = sqlite3.connect('example.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS level_history
               (player text, level text, date text, time real)''')

# # Insert a row of data
# cur.execute("INSERT INTO level_history VALUES ('erik','final','2006-01-05',101)")

cur.execute("DELETE FROM level_history")

# # Save (commit) the changes
# con.commit()

for row in cur.execute('SELECT * FROM level_history'):
    print(row)

print('hello')