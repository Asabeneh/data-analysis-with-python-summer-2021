# What the 10 most frequent words of DONALD J. Trump?

from pprint import pprint
import re
#re.math, re.search, re.findall, re.sub() 

stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 
'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


def read_file(file):
    words = []
    with open(file,'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            line = re.sub(r'[^a-zA-Z ]+',' ', line.lower()).split()
            words += line    
    words_without_stopwords = [w for w in words if w not in stop_words]
    return words_without_stopwords

def find_freq_table(lst, n = 10):
    freq_table = {}
    for x in  lst:
        if x not in freq_table:
            freq_table[x] = 1
        else:
            freq_table[x] = freq_table[x] + 1
    sorted_value = sorted(freq_table.items(), key=lambda x:x[1], reverse=True)
    return sorted_value[:n]

donald_words = read_file('./donald_trump.txt')
obama_words = read_file('./barack_obama.txt')

print('Donald')
pprint(find_freq_table(donald_words, 50))
print('Obama')
pprint( find_freq_table(obama_words, 50))
     



