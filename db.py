import mysql.connector
try:
  db = mysql.connector.connect(
    host="srv938.hstgr.io",
    user="u943517844_racextpy",
    password="Cesar0728.",
    database="u943517844_racextpy"
    )
    if db.is_connected():
      print("conexion exitosa")
cursor = db.cursor()
