#coding : utf-8

import sqlite3

conn = sqlite3.connect('FMailDB.db')
cur = conn.cursor()
cur.execute("select name from sqlite_master where type='table' order by name;")
tables = cur.fetchall()
tables.sort()
# print "111"
print tables