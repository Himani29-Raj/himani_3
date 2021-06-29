import os
from typing import Text

import pickle
from textblob.classifiers import NaiveBayesClassifier,DecisionTreeClassifier,NLTKClassifier
from textblob import TextBlob
os.listdir("datasets")
path="datasets/dev.hi"
records=[]
with open(path,encoding="utf-8",errors="ignores") as f:
    data=f.readlines()
    records.extend(data)
    records[:10]
    path="datasets/test.hii"
with open(path,encoding="utf-8",errors="ignores") as f:
    data=f.readlines()
    records.extend(data)
    len(records)
    datasets=[]
for entry in records:
    try:
        sentence,sentiments=entry.strip().rsplit(',',1)
        datasets.append((sentence,sentiments))
    except:
        pass
len(datasets)
datasets[:10]
train=datasets[:2326]
test=datasets[2326:]

cl = NaiveBayesClassifier(train)
accuracy = cl.accuracy(test)
print("c1>>",accuracy)
print(cl.show_informative_features(5) )


with open("sentiment_classifier_hindi_1.pk",'wb') as f:
    pickle.dump(cl,f)

# cl2 = DecisionTreeClassifier(train)
# accuracy = cl2.accuracy(test)
# print("c2>>",accuracy)
# print(cl2.show_informative_features(5) )
# with open("sentiment_classifier_hindi_2.pk",'wb') as f:
#     pickle.dump(cl2,f)

cl3 = NLTKClassifier(train)
accuracy = cl3.accuracy(test)
print("c3>>",accuracy)
print(cl3.show_informative_features(5) )
with open("sentiment_classifier_hindi_3.pk",'wb') as f:
    pickle.dump(cl3,f)

# test 
blob = TextBlob("उनका निधन भी इसी हादसे में हुआ था।",classifier=cl)
print(blob.classify())