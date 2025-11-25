import spacy


nlp = spacy.load("en_core_web_sm")
def ner(text):
    doc = nlp(text)
    return doc
    
