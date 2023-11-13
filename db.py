import mysql.connector

db = mysql.connector.connect(
    host="185.214.132.8",
    user="u943517844_racextpy",
    password="C0m0erl.",
    database="u943517844_racextpy"
)
cursor = db.cursor()
db.close()