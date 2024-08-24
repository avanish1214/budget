import spacy
from spacy.training import Example

# Create a blank English model
nlp = spacy.blank("en")

# Add NER to the pipeline
ner = nlp.add_pipe("ner")

# Add new labels to the NER
ner.add_label("AMOUNT")
ner.add_label("DATE")
ner.add_label("RECEIVER")
ner.add_label("SENDER")
ner.add_label("TRANSACTION_TYPE")

# Prepare your training data
TRAIN_DATA = [
    ("Dear UPI user A/C X8052 debited by 38.0 on date 20Aug24 trf to TEERTH  SACKLECH Refno 423330665835. If not u? call 1800111109. -SBI", 
     {"entities": [(35, 39, "AMOUNT"), (49, 55, "DATE"), (63, 68, "RECEIVER"), (24, 30, "TRANSACTION_TYPE")]}),
    
    ("Dear SBI User, your A/c X8052-credited by Rs.110 on 19Aug24 transfer from Dev  Sahu Ref No 423203756790 -SBI", 
     {"entities": [(45, 47, "AMOUNT"), (52, 58, "DATE"), (74, 81, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}),
    
    ("Dear SBI User, your A/c X8052-credited by Rs.54 on 18Aug24 transfer from TEERTH  SACKLECHA Ref No 459752004973 -SBI", 
     {"entities": [(45, 46, "AMOUNT"), (51, 57, "DATE"), (73, 86, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}),
    
    ("Dear UPI user A/C X8052 debited by 270.0 on date 18Aug24 trf to SUNEETHA PARASA Refno 423149705369. If not u? call 1800111109. -SBI", 
     {"entities": [(35, 39, "AMOUNT"), (48, 54, "DATE"), (64, 88, "RECEIVER"), (24, 30, "TRANSACTION_TYPE")]}),
    
    ("Dear UPI user A/C X8052 debited by 70.0 on date 16Aug24 trf to MobikwikMerchant Refno 422901525013. If not u? call 1800111109. -SBI", 
     {"entities": [(35,38, "AMOUNT"), (48, 54, "DATE"), (63, 78, "RECEIVER"), (24, 30, "TRANSACTION_TYPE")]}),
    
    ("Dear SBI User, your A/c X8052-credited by Rs.40 on 16Aug24 transfer from SANA  JOSE Ref No 422960541104 -SBI", 
     {"entities": [(45, 46, "AMOUNT"), (51, 57, "DATE"), (73, 81, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}),
    
    ("Dear UPI user A/C X8052 debited by 75.0 on date 16Aug24 trf to munigonda  sunil Refno 422994762203. If not u? call 1800111109. -SBI", 
     {"entities": [(35, 38, "AMOUNT"), (48, 54, "DATE"), (62, 76, "RECEIVER"), (24, 30, "TRANSACTION_TYPE")]}),
    
    ("Dear UPI user A/C X8052 debited by 20.0 on date 13Aug24 trf to TARANI NAGARAJA Refno 422681452193. If not u? call 1800111109. -SBI", 
     {"entities": [(35, 38, "AMOUNT"), (48, 54, "DATE"), (62, 76, "RECEIVER"), (24, 30, "TRANSACTION_TYPE")]}),

    
    (
        "Dear UPI user A/C X8052 debited by 38.0 on date 20Aug24 trf to TEERTH SACKLECH Refno 423330665835. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 38, "AMOUNT"), (49, 55, "DATE"), (64, 78, "RECEIVER"), (24, 30, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear SBI User, your A/c X8052-credited by Rs.110 on 19Aug24 transfer from Dev Sahu Ref No 423203756790 -SBI", 
        {"entities": [(45, 47, "AMOUNT"), (52, 58, "DATE"), (73, 80, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear SBI User, your A/c X8052-credited by Rs.54 on 18Aug24 transfer from TEERTH SACKLECHA Ref No 459752004973 -SBI", 
        {"entities": [(45, 46, "AMOUNT"), (51, 57, "DATE"), (73, 88, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 270.0 on date 18Aug24 trf to SUNEETHA PARASA Refno 423149705369. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 39, "AMOUNT"), (49, 55, "DATE"), (63, 76, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 70.0 on date 16Aug24 trf to MobikwikMerchant Refno 422901525013. If not u? call 1800111109. -SBI", 
        {"entities": [(36, 39, "AMOUNT"), (49, 55, "DATE"), (64, 79, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear SBI User, your A/c X8052-credited by Rs.40 on 16Aug24 transfer from SANA JOSE Ref No 422960541104 -SBI", 
        {"entities": [(45, 46, "AMOUNT"), (51, 57, "DATE"), (73, 81, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 75.0 on date 16Aug24 trf to munigonda sunil Refno 422994762203. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 38, "AMOUNT"), (48, 54, "DATE"), (63, 77, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 20.0 on date 13Aug24 trf to TARANI NAGARAJA Refno 422681452193. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 38, "AMOUNT"), (49, 55, "DATE"), (63, 78, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 25.0 on date 31Jul24 trf to V VENKATESH Refno 421391998781. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 38, "AMOUNT"), (49, 55, "DATE"), (63, 73, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 20.0 on date 31Jul24 trf to V VENKATESH Refno 421392040902. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 38, "AMOUNT"), (49, 55, "DATE"), (63, 73, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 20.0 on date 02Aug24 trf to Subrat Tripathi Refno 421538329553. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 38, "AMOUNT"), (48, 54, "DATE"), (62, 76, "RECEIVER"), (24, 30, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 410.0 on date 02Aug24 trf to KRISHNA RAO K V Refno 421539908395. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 39, "AMOUNT"), (49, 55, "DATE"), (63, 77, "RECEIVER"), (24, 30, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 1150.0 on date 02Aug24 trf to SANA JOSE Refno 421546711602. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 40, "AMOUNT"), (50, 56, "DATE"), (66, 73, "RECEIVER"), (24, 30, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear SBI User, your A/c X8052-credited by Rs.54 on 19Aug24 transfer from NISCHAY AGRAWAL Ref No 423253139228 -SBI", 
        {"entities": [(45, 46, "AMOUNT"), (51, 57, "DATE"), (73, 87, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear SBI User, your A/c X8052-credited by Rs.277 on 19Aug24 transfer from RAHUL SHARMA Ref No 423283324935 -SBI", 
        {"entities": [(45, 47, "AMOUNT"), (52, 58, "DATE"), (74, 85, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear SBI User, your A/c X8052-credited by Rs.37 on 18Aug24 transfer from TEERTH SACKLECHA Ref No 459763211092 -SBI", 
        {"entities": [(45, 46, "AMOUNT"), (51, 57, "DATE"), (73, 89, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 78.94 on date 17Aug24 trf to TEERTH SACKLECH Refno 423011126025. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 39, "AMOUNT"), (49, 55, "DATE"), (62, 76, "RECEIVER"), (24, 30, "TRANSACTION_TYPE")]}
    ),

]





# Train the model
optimizer = nlp.begin_training()
for epoch in range(15):  # Increase the number of epochs if needed
    losses = {}
    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotations)
        nlp.update([example], drop=0.3, losses=losses)
    print(f"Epoch {epoch} - Losses: {losses}")

# Save the trained model
nlp.to_disk("custom_ner_model")
