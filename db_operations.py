import mysql.connector


def connect():
    dbconn = mysql.connector.connect(host="localhost", user="root", password="Leeladhark@905", database='college')
    return dbconn



def insert_data(name,email):
    dbconn = connect()
    mycursor = dbconn.cursor()
    sqlquery = "INSERT INTO boss(name, email) VALUES(%s, %s)"
    val = (name, email)
    mycursor.executemany(sqlquery, val)
    dbconn.commit()
    return (mycursor.rowcount, "record inserted")


result = insert_data("ravi", "ravi@gmail,com"), ("koti", "koti@gmail.com")
print(result)


# def get_data():
#         dbconn = connect()
#         mycursor = dbconn.cursor()
#         mycursor.execute("SELECT * FROM boss")
#         myresult = mycursor.fetchall()
#         for tb in myresult:
#             print(tb)

# def create_db():
#     conndb = connect()
#     mycursor = conndb.cursor()
#     mycursor.execute("CREATE DATABASE god")
#     mycursor.execute("SHOW DATABASES")
#     conndb.commit()
#     for db in mycursor:
#         print(db)



# def create_tb():
#     conndb = connect()
#     mycursor = conndb.cursor()
#     mycursor.execute("CREATE TABLE boys_strength(id int(20), name varchar(32), colour varchar(25))")
#     mycursor.execute("SHOW TABLES")
#     for tb in mycursor:
#         print(tb)



# def drop_database():
#     conndb = connect()
#     mycursor = conndb.cursor()
#     mycursor.execute("DROP DATABASE boys")
#     mycursor.execute("SHOW DATABASES")
#     for tb in mycursor:
#         print(tb)


# def drop_table():
#     conndb = connect()
#     mycursor = conndb.cursor()
#     mycursor.execute("DROP TABLE boys")
#     mycursor.execute("SHOW TABLES")
#     for tb in mycursor:
#         print(tb)


# delete record from table and delete table(all records are deleted in table)
# def delete_record():
#     conndb = connect()
#     mycursor = conndb.cursor()
#     mycursor.execute("DELETE FROM boss WHERE name = 'Mr.lee'")
#     mycursor.execute("SELECT * FROM boss")
#     result = mycursor.fetchall()
#     for allrecords in result :
#         print(allrecords)


# update record in table
# def update_record():
#     conndb = connect()
#     mycursor = conndb.cursor()
#     mycursor.execute("UPDATE boss SET name 'madhu' WHERE name = 'ramu'")
#     mycursor.execute("SELECT * FROM boss")
#     result = mycursor.fetchall()
#     for allrecords in result:
#         print(allrecords)



















