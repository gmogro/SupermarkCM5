import sqlite3
import sql

db = sql.DataBase("supermark.db")
db.update("usuario","estado","0","id_usuario = 1")
db.close()