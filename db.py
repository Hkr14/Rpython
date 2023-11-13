import mysql.connector

db = mysql.connector.connect( host='185.214.132.8', user= 'u943517844_racextpy', passwd='Cesar0728.', db='u943517844_racextpy' )
cur = db.cursor()
cur.execute("SELECT users, FORM id")
for users, id in cur.fetchall():
    print users, id
db.close()