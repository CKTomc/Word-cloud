import string
from nltk.tokenize import word_tokenize as wtk
freq={}
with open("C:\\Users\\khadidja\\Downloads\\word_cloud\\98-0.txt","r",encoding="utf-8") as src:
    data=src.read()
    data=data.replace("“"," ")
    data=data.replace("”"," ")
    data=data.replace("’","'")
    tr = str.maketrans("", "", string.punctuation)
    data1=data.translate(tr)
    data1=data1.lower()
    words=wtk(data1)

with open("C:\\Users\\khadidja\\Downloads\\word_cloud\\stopwords","r") as stopwords:
    stpwrd=stopwords.read()
    stpwrd=stpwrd.lower()
    stpwrd=wtk(stpwrd)

commonwords=list(set(words)&set(stpwrd))
for word in commonwords:
    words=list(filter(lambda w: w != word, words))

for i in range(len(words)):
    if not(words[i] in freq):
        freq[words[i]]=1
    else:
        freq[words[i]]=freq[words[i]]+1

freq=sorted(freq.items(), key=lambda x: x[1], reverse=True)
for i in range (15):
    print (freq[i])
