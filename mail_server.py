import imaplib
import email
from bs4 import BeautifulSoup
import re
import sqlite3
from regex_test import extract_entities

from email_id_processing import get_last_processed_uid, update_last_processed_uid

sql_con=sqlite3.connect('payment_table.db')
cur=sql_con.cursor()

last_processed_uid = get_last_processed_uid()

if last_processed_uid is not None:
    try:
        last_processed_uid = int(last_processed_uid)
    except ValueError:
        print(f"Invalid UID value: {last_processed_uid}")
        last_processed_uid = None  # Handle the error by setting it to None or another fallback action




def get_plain_text(msg):
    plain_text = None

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                plain_text = part.get_payload(decode=True).decode('utf-8')
                break
            elif part.get_content_type() == "text/html":
                html_content = part.get_payload(decode=True).decode('utf-8')
                soup = BeautifulSoup(html_content, "html.parser")
                plain_text = soup.get_text()
                break
    else:
        if msg.get_content_type() == "text/plain":
            plain_text = msg.get_payload(decode=True).decode('utf-8')
        elif msg.get_content_type() == "text/html":
            html_content = msg.get_payload(decode=True).decode('utf-8')
            soup = BeautifulSoup(html_content, "html.parser")
            plain_text = soup.get_text()

    return plain_text


user = "smsbudg@gmail.com"
password = "cuuf wqxb shna jmov"
host = "imap.gmail.com"
imap = imaplib.IMAP4_SSL(host)
imap.login(user, password)
imap.select('Inbox')

# Search for all messages
status, messages = imap.search(None, 'ALL')

email_ids=messages[0].split()
new_email_uids = [uid.decode() for uid in email_ids if last_processed_uid is None or int(uid.decode()) > last_processed_uid]

for email_id in new_email_uids:
    status, data = imap.fetch(email_id, '(RFC822)')
    raw_email=data[0][1]
    msg = email.message_from_bytes(raw_email)
    plain_text = get_plain_text(msg)
    values=extract_entities(plain_text)
    if values:
        if 'RECEIVER' in values:
            values['RECEIVER']=values['RECEIVER'].replace('\r\n', ' ')
            values['RECEIVER']=values['RECEIVER'].split('Refno')[0]
            cur.execute('''INSERT INTO payments (sender, amount, reciever, date) VALUES (?, ?, ?, ?);''',
            ('me', float(values['AMOUNT']), values['RECEIVER'], values['DATE']))

        if 'SENDER' in values:
             values['SENDER']=values['SENDER'].split('Ref No')[0]
             cur.execute('''INSERT INTO payments (sender, amount, reciever, date) VALUES (?, ?, ?, ?);''',
            (values['SENDER'], float(values['AMOUNT']), 'me', values['DATE']))
        
        update_last_processed_uid(email_id)
        print(values)
    sql_con.commit()    

        
    #print(plain_text)
    #print("="*50)
    
    

imap.close()
imap.logout()
