import sqlite3 as DB

connection = DB.connect('bot.db')
cursor = connection.cursor()
connection = DB.connect('bot.db')
cursor = connection.cursor()
temp = cursor.execute("""SELECT * FROM Messages ORDER BY date DESC LIMIT 1""")
print(temp)
raw = cursor.fetchall()
print(raw)
connection.close()
kandidat = list(zip(*raw))
print(*kandidat[1:-2], sep = "\n")





# for element in kandidat[1:-2]:
#     print(*element)

# print('Верно?')


