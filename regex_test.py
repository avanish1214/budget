import re

patterns = {
    "AMOUNT": r"debited by\s?(\d+\.?\d*)|credited by Rs\.(\d+\.?\d*)",  # Amount
    "DATE": r"(?:on|date)\s(\d{2}[A-Za-z]{3}\d{2})",  # Date
    "SENDER": r"transfer from\s+([A-Za-z\s]+)",  # Sender
    "RECEIVER": r"trf to\s+([A-Za-z\s]+)"  # Receiver
}

def extract_entities(text):
    entities = {}
    
    amount_match = re.search(patterns["AMOUNT"], text)
    if amount_match:
        entities["AMOUNT"] = amount_match.group(1)
    
    
    date_match = re.search(patterns["DATE"], text)
    if date_match:
        entities["DATE"] = date_match.group(1)
    
    
    sender_match = re.search(patterns["SENDER"], text)
    if sender_match:
        entities["SENDER"] = sender_match.group(1).strip()
    
    receiver_match = re.search(patterns["RECEIVER"], text)
    if receiver_match:
        entities["RECEIVER"] = receiver_match.group(1).strip()
    
    return entities

test="Dear UPI user A/C X8052 debited by 38.0 on date 20Aug24 trf to TEERTH SACKLECH Refno 423330665835."
ent=extract_entities(test)
print(ent)