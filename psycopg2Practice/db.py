import psycopg2

def createTable():
    connection = psycopg2.connect("dbname='testdb' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = psycopg2.connect("dbname='testdb' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price))
    connection.commit()
    connection.close()


def view():
    connection = psycopg2.connect("dbname='testdb' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    connection.close()
    return rows

def delete(item):
    connection = psycopg2.connect("dbname='testdb' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM store WHERE item=?", (item,))
    connection.commit()
    connection.close()


def update(item, quantity, price):
    connection = psycopg2.connect("dbname='testdb' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = connection.cursor()
    cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    connection.commit()
    connection.close()

createTable()
insert('Tesla', 12, 123456)
print(view())
