import sqlite3

conn = sqlite3.connect("Artistc.db")
cursor =  conn.cursor()
#Question #1. How many artists are represented in the database? 
cursor.execute('SELECT * FROM artists')
data = cursor.fetchall()
print('Number of artists in the database:', len(data))

#Question #2. How many women (Female) are in the database?
cursor.execute('SELECT * FROM artists where Gender == "Female"')
data1 = cursor.fetchall()
print('Number of women in the database:', len(data1))

#Question #3. How many people in the database were born before 1900?
cursor.execute('SELECT * FROM artists where "Birth Year" < 1900')
data2 = cursor.fetchall()
print('Number of people born before 1900 in the database:', len(data2))

#Question #4*. What is the name of the oldest artist?
oldest = {'name': '', 'birthday': 1900}
for person in data2:
    if person[4] < oldest['birthday']:
        oldest['name'] = person[1]
        oldest['birthday'] = person[4]
print('The oldest:', oldest)

