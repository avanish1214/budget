import csv
import sqlite3
con=sqlite3.connect("budget.db")
cur=con.cursor()

cur.execute('''DROP TABLE IF EXISTS PAYMENT''')

query=''' CREATE TABLE PAYMENT(
    Payid VARCHAR[20] PRIMARY KEY,
    Expenses INT,
    reciever VARCHAR[30],
    dt date,
    sender VARCHAR[30],
    Type VARCHAR[30],
    Mode VARCHAR[30],
    Settlement VARCHAR[10]
);'''
cur.execute(query)



with open ('payment.csv', mode='r') as file:
    csvFile=csv.reader(file)



    for line1 in csvFile:
        print(line1)
        cur.execute(f"INSERT INTO PAYMENT VALUES('{line1[0]}',{int(line1[1])},'{line1[2]}',DATE('now'), '{line1[4]}', '{line1[5]}', '{line1[6]}','{line1[7]}');")
        con.commit()
file.close()


cur.execute('''DROP TABLE IF EXISTS FIXEDPAYMENT''')


query1='''CREATE TABLE FIXEDPAYMENT(
    PAYEE VARCHAR[20],
    SENDER VARCHAR[20],
    TYPE VARCHAR[20],
    ESTAMT INT,
    DT DATE,
    PAYMENTNO INT,
    PERCENTINCREASE INT,
    PAYMENT INT,
    PAYMENTID VARCHAR[20]);'''
cur.execute(query1)

with open('fixedpayment.csv', mode='r')as file:
    mycsvFile=csv.reader(file)
    for line in mycsvFile:
        print(line)
        cur.execute(f"INSERT INTO FIXEDPAYMENT VALUES('{line[0]}','{line[1]}','{line[2]}','{int(line[3])}',DATE('now') ,'{int(line[4])}', '{int(line[5])}', '{int(line[6])}','{line[7]}');")
        con.commit()
file.close()


cur.execute('''DROP TABLE IF EXISTS LOAN''')

query2='''CREATE TABLE LOAN(
    LOANID VARCHAR[20] PRIMARY KEY,
    [BANK NAME] VARCHAR[20],
    [LOAN PAYEE] VARCHAR[20],
    [LOAN PURPOSE] VARCHAR[30],
    TENURE INT,
    ROI INT,
    PMI INT,
    [INSTALLMENTS PAID] INT,
    [LOAN STATUS] VARCHAR[20],
    [REM INSTALLMENTS] INT,
    DT DATE,
    BLID VARCHAR[20]);'''
cur.execute(query2)

with open('loan.csv', mode='r')as file:
    mycsvFile1=csv.reader(file)
    for line in mycsvFile1:
        print(line)
        cur.execute(f"INSERT INTO LOAN VALUES('{line[0]}','{line[1]}','{line[2]}','{line[3]}', '{int(line[4])}', '{int(line[5])}', '{int(line[6])}','{int(line[7])}','{line[8]}',{int(line[9])},DATE('now'),'{line[10]}');")
        con.commit()
file.close()


cur.execute("DROP TABLE IF EXISTS SAVINGS")

query3='''CREATE TABLE SAVINGS(
    PAYMENTID VARCHAR[20],
    PAYEE VARCHAR[20],
    AMOUNT INT,
    DT DATE,
    [DEBIT/CREDIT] INT);'''
cur.execute(query3)

with open('savings.csv', mode='r') as file:
    myFile=csv.reader(file)
    for line in myFile:
        cur.execute(f"INSERT INTO SAVINGS VALUES('{line[0]}','{line[1]}','{int(line[2])}', DATE('now'), '{int(line[3])}');")
        con.commit()
file.close()
