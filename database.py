import mysql.connector

def get_data():
    mydb =mysql.connector.connect(user="root",password="9633401920m",database="testdb")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT * FROM employee")
    result=mycursor.fetchmany()
    mydb.close()
    return result