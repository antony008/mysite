import sqlite3  
conn = sqlite3.connect('myshop.db')

def createProductIable(conn):
    c = conn.cursor()
    sql = """
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        qty INTEGER NOT NULL
    )
    """
    c.execute(sql)
    conn.commit()
def insertProducts(conn, name, price, qty):
    c = conn.cursor()
    sql = """
    INSERT INTO products (name, price, qty)
    VALUES (?, ?, ?)
    """
    #c.execute(sql, ('Pen', 15, 45))
    #c.execute(sql, ('Cup', 80, 5))
    #c.execute(sql, ('Notebook', 25, 20))
    c.execute(sql, (name, price, qty))
    conn.commit()

def listProducts(conn, Where):
    c = conn.cursor()
    sql = '''
    SELECT id, name, price, qty FROM products 
        Where {}
        '''.format(Where)
    c.execute(sql)
    pds = c.fetchall()
    for pd in pds:
        print(pd)

def getProducts(conn):
    c = conn.cursor()
    sql = '''
    SELECT id, name, price, qty FROM products 
        
        '''
    c.execute(sql)
    return c.fetchall()

def update_product(conn, id, price, qty):  
    sql = """
        UPDATE products
        SET price = ?,
            qty = ?
        WHERE id = ?
    """
    c = conn.cursor()
    c.execute(sql, (price, qty, id))
    conn.commit()

def delete_by_id(conn, id):
    sql="""
    DELETE FROM products WHERE id = ?
    """
    conn.execute(sql, (id,))
    conn.commit    

def test():
    #createProductIable(conn)
    #insertProduct(conn, 'Stapler', 100, 10)
    #insertProduct(conn, 'card', 15, 3)
    #insertProduct(conn, 'pen', 15, 3)
    #insertProduct(conn, 'pencil', 5, 3)
    update_product(conn, 1, 40, 2)
    #delete_by_id(conn, 1)
    listProducts(conn, 'price > 0')
    conn.close()

test()