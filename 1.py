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
    ("Dear SBI UPI User, ur A/cX8052 credited by Rs1150 on 26Jul24 by  (Ref no 420876918966)", 
        {"entities": [(29, 35, "ACCOUNT"), (45, 51, "AMOUNT"), (55, 62, "DATE"), (70, 84, "REF_NO")]}),
    
    ("Dear SBI UPI User, ur A/cX8052 credited by Rs2310 on 26Jul24 by  (Ref no 420859729754)", 
        {"entities": [(29, 35, "ACCOUNT"), (45, 51, "AMOUNT"), (55, 62, "DATE"), (70, 84, "REF_NO")]}),
    
    ("Dear SBI UPI User, ur A/cX8052 credited by Rs1260 on 26Jul24 by  (Ref no 420860156671)", 
        {"entities": [(29, 35, "ACCOUNT"), (45, 51, "AMOUNT"), (55, 62, "DATE"), (70, 84, "REF_NO")]}),
    
    ("Dear UPI user A/C X8052 debited by 25.0 on date 31Jul24 trf to V VENKATESH Refno 421391998781. If not u? call 1800111109. -SBI", 
        {"entities": [(19, 25, "ACCOUNT"), (36, 40, "AMOUNT"), (49, 56, "DATE"), (60, 71, "RECEIVER"), (78, 92, "REF_NO")]}),
    
    ("Dear UPI user A/C X8052 debited by 250.0 on date 01Aug24 trf to ASHOKA V  . Refno 421495302295. If not u? call 1800111109. -SBI", 
        {"entities": [(19, 25, "ACCOUNT"), (36, 42, "AMOUNT"), (51, 58, "DATE"), (62, 70, "RECEIVER"), (79, 93, "REF_NO")]}),
    
    ("Dear UPI user A/C X8052 debited by 50.0 on date 08Aug24 trf to ISTHARA PARKS PR Refno 422108370947. If not u? call 1800111109. -SBI", 
        {"entities": [(19, 25, "ACCOUNT"), (36, 40, "AMOUNT"), (49, 56, "DATE"), (60, 77, "RECEIVER"), (84, 98, "REF_NO")]}),
    
    ("Dear UPI user A/C X8052 debited by 80.0 on date 08Aug24 trf to ISTHARA PARKS PR Refno 422108672493. If not u? call 1800111109. -SBI", 
        {"entities": [(19, 25, "ACCOUNT"), (36, 40, "AMOUNT"), (49, 56, "DATE"), (60, 77, "RECEIVER"), (84, 98, "REF_NO")]}),
    
    ("Dear UPI user A/C X8052 debited by 10.0 on date 04Aug24 trf to THUMKUNTA SRIDHA Refno 421768925466. If not u? call 1800111109. -SBI", 
        {"entities": [(19, 25, "ACCOUNT"), (36, 40, "AMOUNT"), (49, 56, "DATE"), (60, 76, "RECEIVER"), (83, 97, "REF_NO")]}),
    
    ("Dear UPI user A/C X8052 debited by 12.0 on date 08Aug24 trf to VIJAYA  SANNI Refno 422196569615. If not u? call 1800111109. -SBI", 
        {"entities": [(19, 25, "ACCOUNT"), (36, 40, "AMOUNT"), (49, 56, "DATE"), (60, 73, "RECEIVER"), (80, 94, "REF_NO")]}),
    
    ("Dear UPI user A/C X8052 debited by 83.0 on date 17Aug24 trf to Agarwal Super Ma Refno 423012403554. If not u? call 1800111109. -SBI", 
        {"entities": [(19, 25, "ACCOUNT"), (36, 40, "AMOUNT"), (49, 56, "DATE"), (60, 76, "RECEIVER"), (83, 97, "REF_NO")]}),
    
    ("Dear SBI User, your A/c X8052-credited by Rs.37 on 18Aug24 transfer from TEERTH  SACKLECHA Ref No 459763211092 -SBI", 
        {"entities": [(22, 27, "ACCOUNT"), (41, 46, "AMOUNT"), (50, 57, "DATE"), (71, 87, "SENDER"), (95, 109, "REF_NO")]}),
    
    ("Dear SBI User, your A/c X8052-credited by Rs.54 on 19Aug24 transfer from NISCHAY  AGRAWAL Ref No 423253139228 -SBI", 
        {"entities": [(22, 27, "ACCOUNT"), (41, 46, "AMOUNT"), (50, 57, "DATE"), (71, 86, "SENDER"), (94, 108, "REF_NO")]}),
    
    ("Dear UPI user A/C X8052 debited by 83.0 on date 17Aug24 trf to Agarwal Super Ma Refno 423012403554. If not u? call 1800111109. -SBI",
        {"entities": [(19, 25, "ACCOUNT"), (36, 40, "AMOUNT"), (49, 56, "DATE"), (60, 76, "RECEIVER"), (83, 97, "REF_NO")]}),
    
    ("Dear UPI user A/C X8052 debited by 25.0 on date 31Jul24 trf to V VENKATESH Refno 421391998781. If not u? call 1800111109. -SBI",
        {"entities": [(19, 25, "ACCOUNT"), (36, 40, "AMOUNT"), (49, 56, "DATE"), (60, 71, "RECEIVER"), (78, 92, "REF_NO")]}),
    
    ("Dear UPI user A/C X8052 debited by 250.0 on date 01Aug24 trf to ASHOKA V  . Refno 421495302295. If not u? call 1800111109. -SBI",
        {"entities": [(19, 25, "ACCOUNT"), (36, 42, "AMOUNT"), (51, 58, "DATE"), (62, 70, "RECEIVER"), (79, 93, "REF_NO")]}),
    
    ("Dear SBI User, your A/c X8052-credited by Rs.37 on 18Aug24 transfer from TEERTH  SACKLECHA Ref No 459763211092 -SBI",
        {"entities": [(22, 27, "ACCOUNT"), (41, 46, "AMOUNT"), (50, 57, "DATE"), (71, 87, "SENDER"), (95, 109, "REF_NO")]}),
    
    ("Dear SBI User, your A/c X8052-credited by Rs.54 on 19Aug24 transfer from NISCHAY  AGRAWAL Ref No 423253139228 -SBI",
        {"entities": [(22, 27, "ACCOUNT"), (41, 46, "AMOUNT"), (50, 57, "DATE"), (71, 86, "SENDER"), (94, 108, "REF_NO")]}),
    
    ("Dear SBI User, your A/c X8052-credited by Rs.67 on 25Aug24 transfer from SAUMIL  SHAH Ref No 423253159013 -SBI",
        {"entities": [(22, 27, "ACCOUNT"), (41, 46, "AMOUNT"), (50, 57, "DATE"), (71, 82, "SENDER"), (90, 104, "REF_NO")]}),
    
    ("Dear SBI User, your A/c X8052-credited by Rs.121 on 26Aug24 transfer from ADITYA  SINGH Ref No 423253175029 -SBI",
        {"entities": [(22, 27, "ACCOUNT"), (42, 48, "AMOUNT"), (52, 59, "DATE"), (73, 84, "SENDER"), (92, 106, "REF_NO")]}),
    
    ("Dear SBI UPI User, ur A/cX8052 credited by Rs1150 on 26Jul24 by  (Ref no 420876918966)",
        {"entities": [(29, 35, "ACCOUNT"), (45, 51, "AMOUNT"), (55, 62, "DATE"), (70, 84, "REF_NO")]}),
    
    ("Dear SBI UPI User, ur A/cX8052 credited by Rs2310 on 26Jul24 by  (Ref no 420859729754)",
        {"entities": [(29, 35, "ACCOUNT"), (45, 51, "AMOUNT"), (55, 62, "DATE"), (70, 84, "REF_NO")]}),
    
    ("Dear SBI UPI User, ur A/cX8052 credited by Rs1260 on 26Jul24 by  (Ref no 420860156671)",
        {"entities": [(29, 35, "ACCOUNT"), (45, 51, "AMOUNT"), (55, 62, "DATE"), (70, 84, "REF_NO")]}),


    (
        "Dear UPI user A/C X8052 debited by 38.0 on date 20Aug24 trf to TEERTH SACKLECH Refno 423330665835. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 39, "AMOUNT"), (49, 55, "DATE"), (64, 78, "RECEIVER"), (24, 30, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear SBI User, your A/c X8052-credited by Rs.110 on 19Aug24 transfer from Dev Sahu Ref No 423203756790 -SBI", 
        {"entities": [(45, 50, "AMOUNT"), (52, 58, "DATE"), (73, 81, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear SBI User, your A/c X8052-credited by Rs.54 on 18Aug24 transfer from TEERTH SACKLECHA Ref No 459752004973 -SBI", 
        {"entities": [(45, 49, "AMOUNT"), (51, 57, "DATE"), (73, 86, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 270.0 on date 18Aug24 trf to SUNEETHA PARASA Refno 423149705369. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 40, "AMOUNT"), (49, 55, "DATE"), (64, 77, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 70.0 on date 16Aug24 trf to MobikwikMerchant Refno 422901525013. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 39, "AMOUNT"), (49, 55, "DATE"), (64, 79, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear SBI User, your A/c X8052-credited by Rs.40 on 16Aug24 transfer from SANA JOSE Ref No 422960541104 -SBI", 
        {"entities": [(45, 49, "AMOUNT"), (51, 57, "DATE"), (73, 81, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 75.0 on date 16Aug24 trf to munigonda sunil Refno 422994762203. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 39, "AMOUNT"), (48, 54, "DATE"), (62, 76, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 20.0 on date 13Aug24 trf to TARANI NAGARAJA Refno 422681452193. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 39, "AMOUNT"), (48, 54, "DATE"), (62, 76, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 25.0 on date 31Jul24 trf to V VENKATESH Refno 421391998781. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 39, "AMOUNT"), (49, 55, "DATE"), (63, 73, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 20.0 on date 31Jul24 trf to V VENKATESH Refno 421392040902. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 39, "AMOUNT"), (49, 55, "DATE"), (63, 73, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 20.0 on date 02Aug24 trf to Subrat Tripathi Refno 421538329553. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 39, "AMOUNT"), (48, 54, "DATE"), (62, 76, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 410.0 on date 02Aug24 trf to KRISHNA RAO K V Refno 421539908395. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 39, "AMOUNT"), (49, 55, "DATE"), (63, 77, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 1150.0 on date 02Aug24 trf to SANA JOSE Refno 421546711602. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 40, "AMOUNT"), (50, 56, "DATE"), (66, 73, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear SBI User, your A/c X8052-credited by Rs.54 on 19Aug24 transfer from NISCHAY AGRAWAL Ref No 423253139228 -SBI", 
        {"entities": [(45, 49, "AMOUNT"), (51, 57, "DATE"), (73, 87, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear SBI User, your A/c X8052-credited by Rs.277 on 19Aug24 transfer from RAHUL SHARMA Ref No 423283324935 -SBI", 
        {"entities": [(45, 50, "AMOUNT"), (52, 58, "DATE"), (74, 85, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear SBI User, your A/c X8052-credited by Rs.37 on 18Aug24 transfer from TEERTH SACKLECHA Ref No 459763211092 -SBI", 
        {"entities": [(45, 49, "AMOUNT"), (51, 57, "DATE"), (73, 89, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}
    ),
    (
        "Dear UPI user A/C X8052 debited by 78.94 on date 17Aug24 trf to TEERTH SACKLECH Refno 423011126025. If not u? call 1800111109. -SBI", 
        {"entities": [(35, 40, "AMOUNT"), (49, 55, "DATE"), (62, 76, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}
    ),


    ("Dear UPI user A/C X8052 debited by 38.0 on date 20Aug24 trf to TEERTH SACKLECH Refno 423330665835. If not u? call 1800111109. -SBI", 
     {"entities": [(35, 39, "AMOUNT"), (49, 55, "DATE"), (64, 78, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}),
    
    ("Dear SBI User, your A/c X8052-credited by Rs.110 on 19Aug24 transfer from Dev Sahu Ref No 423203756790 -SBI", 
     {"entities": [(45, 50, "AMOUNT"), (52, 58, "DATE"), (73, 81, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}),
    
    ("Dear SBI User, your A/c X8052-credited by Rs.54 on 18Aug24 transfer from TEERTH SACKLECHA Ref No 459752004973 -SBI", 
     {"entities": [(45, 49, "AMOUNT"), (51, 57, "DATE"), (73, 86, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}),
    
    ("Dear UPI user A/C X8052 debited by 270.0 on date 18Aug24 trf to SUNEETHA PARASA Refno 423149705369. If not u? call 1800111109. -SBI", 
     {"entities": [(35, 40, "AMOUNT"), (49, 55, "DATE"), (64, 77, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}),
    
    ("Dear UPI user A/C X8052 debited by 70.0 on date 16Aug24 trf to MobikwikMerchant Refno 422901525013. If not u? call 1800111109. -SBI", 
     {"entities": [(35, 39, "AMOUNT"), (49, 55, "DATE"), (64, 79, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}),
    
    ("Dear SBI User, your A/c X8052-credited by Rs.40 on 16Aug24 transfer from SANA JOSE Ref No 422960541104 -SBI", 
     {"entities": [(45, 49, "AMOUNT"), (51, 57, "DATE"), (73, 81, "SENDER"), (30, 37, "TRANSACTION_TYPE")]}),
    
    ("Dear UPI user A/C X8052 debited by 75.0 on date 16Aug24 trf to munigonda sunil Refno 422994762203. If not u? call 1800111109. -SBI", 
     {"entities": [(35, 39, "AMOUNT"), (48, 54, "DATE"), (62, 76, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}),
    
    ("Dear UPI user A/C X8052 debited by 20.0 on date 13Aug24 trf to TARANI NAGARAJA Refno 422681452193. If not u? call 1800111109. -SBI", 
     {"entities": [(35, 39, "AMOUNT"), (48, 54, "DATE"), (62, 76, "RECEIVER"), (24, 31, "TRANSACTION_TYPE")]}),
    
    # Add more examples as needed
]

# Train the NER model
pipe_exceptions = ["ner"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

with nlp.disable_pipes(*unaffected_pipes):
    optimizer = nlp.begin_training()  # Use begin_training() instead of resume_training()

    for epoch in range(15):  # Number of training epochs
        losses = {}
        for text, annotations in TRAIN_DATA:
            example = Example.from_dict(nlp.make_doc(text), annotations)
            nlp.update([example], drop=0.2, losses=losses)  # Lowered drop to 0.2

        print(f"Epoch {epoch + 1} - Losses: {losses}")
nlp.to_disk("custom_ner_model_1")