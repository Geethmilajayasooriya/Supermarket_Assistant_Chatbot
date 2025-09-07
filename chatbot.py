import spacy

nlp = spacy.load("en_core_web_sm")

product_shelf = {
    "apple": "Shelf 1",
    "orange" : "Shelf 1",
    "banana" : "Shelf 1",
    "bread": "Shelf 2",
    "buns": "Shelf 2",
    "milk": "Shelf 3",
    "eggs": "Shelf 3",
    "butter": "Shelf 3",
    "chocolate": "Shelf 4",
    "ice cream": "Shelf 4",
    "yourgert": "Shelf 4",
    "soap": "Shelf 5",
    "shampoo": "Shelf 5",
    "toothpaste": "Shelf 5",
    "rice": "Shelf 6",
    "cereal": "Shelf 6",
     "dhal": "Shelf 6"
}

def extract_items(text):
    doc = nlp(text)
   
    return [token.lemma_.lower() for token in doc if token.pos_ in ("NOUN", "PROPN")]


def find_shelves(items):
    result = {}
    for item in items:
        result[item] = product_shelf.get(item, "Item not found")
    return result
