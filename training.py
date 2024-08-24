import spacy
nlp = spacy.load("custom_ner_model_1")

# Test the model with some example texts
test_texts = [
    "Dear UPI user A/C X8052 debited by 38.0 on date 20Aug24 trf to TEERTH SACKLECH Refno 423330665835.",
    "Dear SBI User, your A/c X8052-credited by Rs.110 on 19Aug24 transfer from Dev Sahu Ref No 423203756790.",
    "Dear SBI User, your A/c X8052-credited by Rs.54 on 18Aug24 transfer from TEERTH SACKLECHA Ref No 459752004973.",
    "Dear UPI user A/C X8052 debited by 38.0 on date 20Aug24 trf to TEERTH  SACKLECH Refno 423330665835. If not u? call 1800111109. -SBI"
]

for text in test_texts:
    doc = nlp(text)
    print(f"Text: {text}")
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Label: {ent.label_}")
    print("\n")

