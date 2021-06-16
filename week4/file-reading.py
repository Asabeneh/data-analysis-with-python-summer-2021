f = open('./donald.txt')
lines = f.read().splitlines()

words = []
for line in lines:
    temp_words = line.lower().strip().replace('.', '').split()
    for w in temp_words:
        if w not in words:
            words.append(w)
print(words)



from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print(stop_words)

# Without removing anystop words make a word frequency table and find the 10 most frequent words he used during the inagurration
# remove the stop words and count the total number of unique numbers



