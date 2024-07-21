import hashlib
import time
# Include SQLITE3 when modifying is_valid_token
import sqlite3
from Db_creation import create_sqlite_database
creds = {}
login_window = 10


sql_con=sqlite3.connect('login_info.db')
sql_cursor=sql_con.cursor()

sql_cursor.execute('''CREATE TABLE IF NOT EXISTS CREDENTIALS(username VARCHAR[20], sessionid VARCHAR[50], password VARCHAR[20], time FLOAT);''')




def update_credentials(username, password_hash, session_id):
    """
        The function updates the user credentials source that will be checked for by the function is_valid_token.
    """
    if password_hash != "":
        #creds[username] = {"hash": password_hash}
        sql_cursor.execute(f"UPDATE CREDENTIALS SET password='{password_hash}'  WHERE username='{username}'")
        sql_con.commit()
    if session_id != "":
        #creds[username].update({"last_session": session_id, "last_login": time.time()})
        sql_cursor.execute(f"UPDATE CREDENTIALS SET sessionid='{session_id}',time='{time.time()}' WHERE username='{username}'")
        sql_con.commit()

def register_user(username, password_hash):
    """
        The function adds credentials for a new user and returns the Session ID.
    """
    #if username in creds:
        #return False
    #session_id=str(get_session_id(username," "))

    sql_cursor.execute(f"select * from CREDENTIALS where username='{username}'")
    values=sql_cursor.fetchall()
    if values==[]:
        sql_cursor.execute(f"INSERT INTO CREDENTIALS VALUES('{username}','','{password_hash}','{time.time()}')")
        #update_credentials(username, password_hash, "Registered")
        sql_con.commit()
        create_sqlite_database(username)
        #sql_con.close()
        return True
    return False
    


def get_session_id(username='', password_hash=''):
    """
        This function generates the session ID based on the username and password hash.
    """
    m = hashlib.sha256()
    m.update(username.encode())
    m.update(password_hash.encode())
    return m.hexdigest()


def login_user(username, password_hash):
    """
        This function calls the functions to get a session ID for existing users only.
    """
    sql_cursor.execute(f"SELECT * FROM CREDENTIALS WHERE username='{username}'; ")
    validation_info=sql_cursor.fetchall()
    if validation_info==[]:
        return False,""
    else:
        pwd=validation_info[0][2]
        if pwd==password_hash:
            session_id=get_session_id(username,"")
            update_credentials(username,"",session_id)
            return True,session_id
        else:
            return False, ""
    '''if username in creds and password_hash == creds[username]["hash"]:
        session_id = get_session_id()
        update_credentials(username, "", session_id)
        return True, session_id
    return False, "" '''


def is_valid_token(sessionid, username):
    """
        This function checks if the session ID and username are valid.
    """
    # Update with the table login.
    
    sql_cursor.execute(f"SELECT sessionid,time FROM CREDENTIALS WHERE username='{username}';")
    response=sql_cursor.fetchall()
    if response==[]:
        return False
    last_session=response[0][0]
    last_login=response[0][1]
    if last_session==sessionid:
        if((time.time()-last_login)<login_window):
            update_credentials(username, "", sessionid)
            return True
    return False



    if username in creds:
        if "last_session" in creds[username]:
            if sessionid == creds[username]["last_session"]:
                if (time.time() - creds[username]["last_login"]) < login_window:
                    creds[username]["last_login"] = time.time()
                    return True
                creds.pop(username)
    return False

