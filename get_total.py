import sqlite3



def calculate_total():
    sql_con=sqlite3.connect('payment_table.db')
    totalamount=0
    cur=sql_con.cursor()
    cur.execute('''select * from payments''')
    data=cur.fetchall()
    print(data)
    
    for i in data:
        if(i[0]=='me'):
            totalamount=totalamount+i[1]
        else:
            totalamount=totalamount-i[1] 
    return totalamount
    
print(calculate_total())