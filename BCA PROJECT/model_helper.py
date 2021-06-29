import pickle
import os

from textblob import TextBlob


def load(path=r'classifier_model\sentiment_classifier_hindi.pk'):
    with open(path,'rb') as file:
        return pickle.load(file)

if __name__ == "__main__":
    cl = load()

    blob = TextBlob("उनका निधन भी इसी हादसे में हुआ था।",classifier=cl)
    print(blob.detect_language())
    print([np for np in blob.noun_phrases])
    print(blob.classify())

    