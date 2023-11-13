import mysql.connector

db = mysql.connector.connect( host='185.214.132.8', user= 'u943517844_racextpy', passwd='Cesar0728.', db='u943517844_racextpy' )
cur = db.cursor()
db.close()