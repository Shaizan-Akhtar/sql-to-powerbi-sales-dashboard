import pymysql as p 

def db_connect() : 
    return p.connect(host="localhost", user="root", password="", database="sales_db")

def create_tbl ():
    db = db_connect()
    cr = db.cursor()

    table = input("What will be your table name ?\n")

    col = int(input("How many col do you want in your table ? \n"))
    count = 1

    columns = []
    while count <= col:
        column_detail = input("Please enter the column details ?\n")
        columns.append(column_detail)
        count += 1


    cr.execute(f"create table {table} ({",".join(columns)})")

def drop_tbl():
    db = db_connect()
    cr = db.cursor()

    table_name = input("Which table you want to drop ?\n")

    cr.execute(f"drop table {table_name}")

create_tbl()
drop_tbl()