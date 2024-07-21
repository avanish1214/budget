from tables import tables
import sqlite3

def create_tables(db_name):
    try:   
        con=sqlite3.connect(db_name)
        cur=con.cursor()
        for table_name in tables:
            parameters = tables[table_name]
            table_drop_query = "DROP TABLE IF EXISTS {table_name}"
            table_create_query = "CREATE TABLE {table_name}({parameters});"
            cur.execute(table_drop_query.format(table_name=table_name))
            cur.execute(table_create_query.format(table_name=table_name,parameters=parameters))
        print(f"{len(tables)} created in {table_name}")
        con.commit()
        con.close()
        return True
    except Exception as e:
        print(f"Error occured while running create_tables on {db_name}: {e}")
    return False

