import mysql.connector

db = mysql.connector.connect(
  host='',
  user= 'u943517844_racextpy',
  passwd='Cesar0728.', 
  database='u943517844_racextpy' )
cur = db.cursor()
db.close()
import mysql.connector

db = mysql.connector.connect(
    host="185.214.132.8",
    user="root",
    password="",
    database="BUENO"
)
cursor = db.cursor()