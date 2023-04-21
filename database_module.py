import mysql.connector


def select():
    # connect to database mysql with using connect() function
    conndb = mysql.connector.connect(host='localhost', user='root', password='Leeladhark@905', database='university')

    # create mycursor object with using cursor() function for execute a query
    mycursor = conndb.cursor()
    mycursor.execute("SELECT * FROM sports")

    # fetch the results
    results = mycursor.fetchall()

    # close the conndb
    conndb.close()

    # return the results
    return results


if __name__ == '__main__':
    o = select()
# print(o)



#  -------------------------------------------------------------------------------------------------------------
# import mysql.connector
#
# def connect():
#     conndb = mysql.connector.connect(host='localhost', user ='root', password='Leeladhark@905')
#     return conndb
#
#
# def create():
#     mydb = connect()
#     mycursor = mydb.cursor()
#     mycursor.execute("CREATE DATABASE fruits")








