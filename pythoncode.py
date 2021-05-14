from googletrans import Translator

def dictionary():
    translator=Translator()

    word=input()
    print((translator.translate(word, src='en', dest='fr')).text)
dictionary()

