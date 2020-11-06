import mysql.connector  #creation of data base

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Aman@123"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE aman")
mycursor.execute("CREATE TABLE Project (GBX_ID VARCHAR(9), Fullname VARCHAR(40), ACC_AXIS VARCHAR(10), contact VARCHAR(10), email_id VARCHAR(50), username VARCHAR(50), password VARCHAR(4), ACC_ICICI VARCHAR(10), ACC_HDFC VARCHAR(10), ACC_CBI VARCHAR(10))")





mycursor.execute("CREATE TABLE Bank (acc_no VARCHAR(10) PRIMARY KEY, BGBX_ID VARCHAR(9), FILE_NAME VARCHAR (20))")
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Aman@123",
  database="aman"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Project (GBX_ID VARCHAR(9), Fullname VARCHAR(40), ACC_AXIS VARCHAR(10), contact VARCHAR(10), email_id VARCHAR(50), username VARCHAR(50), password VARCHAR(4), ACC_ICICI VARCHAR(10), ACC_HDFC VARCHAR(10), ACC_CBI VARCHAR(10))")
mycursor.execute("CREATE TABLE Bank (acc_no VARCHAR(10) PRIMARY KEY, BGBX_ID VARCHAR(9), FILE_NAME VARCHAR (20))")
sql = "INSERT INTO Project (GBX_ID, Fullname,ACC_AXIS,contact,email_id,username,password,ACC_ICICI,ACC_HDFC,ACC_CBI) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"


#val = ("GBXA0AM06", "Aman Shukla",      "8143762821","9452076406","aman.shukla200115@gmail.com","IamAman"   ,"5847","7362829178", "2136287872", "9628178732")
#mycursor.execute(sql,val)
print("1 row inserted ")



mycursor.execute(sql)

mydb.commit()