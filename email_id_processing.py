def get_last_processed_uid():
    try:
        with open('last_uid.txt', 'r') as file:
            uid = file.read().strip()  
            if uid:  
                return uid
            else:
                return None  
    except FileNotFoundError:
        return None

def update_last_processed_uid(uid):
    if isinstance(uid, bytes):  
        uid = uid.decode('utf-8')  
    if uid:  
        with open('last_uid.txt', 'w') as file:
            file.write(uid)
