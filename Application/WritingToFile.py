import sqlite3
from sqlite3 import Error

def insert_into_db(fname, lname, outdoor=1, indoor=1, manage=0, desired_hours=40):
  conn = sqlite3.connect(r'Schedulerdatabase.db')
  c = conn.cursor()

  sql = ''' INSERT INTO employee(fname, lname, outdoor, indoor, manage, hours)
                VALUES(?,?,?,?,?,?) '''
  employee_truncated = (fname, lname, outdoor, indoor, manage, desired_hours)
  c.execute(sql, employee_truncated)
  conn.commit()
  conn.close()

def delete(id):
  conn = sqlite3.connect(r'Schedulerdatabase.db')
  c = conn.cursor()

  sql = 'DELETE FROM employee WHERE id=?'
  c.execute(sql, (id,))
  conn.commit()
  conn.close()

def read_table(id):
  conn = sqlite3.connect(r'Schedulerdatabase.db')
  c = conn.cursor()
  c.execute('SELECT * FROM employee WHERE id=?',(id,))
  rows = c.fetchall()

  for row in rows:
    return(row)

def quack():
  print('quack')

#
# for i in range(100):
#   insert_into_db('John'+str(i), 'Fortnite')
#
# for i in range(100):
#   read_table(i)