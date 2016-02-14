from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
import numpy as np
import pdb
from itertools import izip
from scipy.sparse import coo_matrix
import nltk 
from nltk.stem import SnowballStemmer, WordNetLemmatizer
import codecs
import sys

def sort_sparse(m):
    m = coo_matrix(m)
    tuples = izip(m.row, m.col, m.data)
    return sorted(tuples, key=lambda x: x[2], reverse=True)

def open_lemmatize(fileName):
    lemmatizer = WordNetLemmatizer()
    processed_doc = ""
    with open(fileName, "r", encoding="utf8") as infile:
        for word in infile.read():
            processed_doc += lemmatizer.lemmatize(word)

    return processed_doc

reload(sys)
sys.setdefaultencoding('utf8')

#fordoc = open_lemmatize("doc1.txt")
#agdoc = open_lemmatize("")
doc1 = open('data/doc1.txt','r')
doc2 = open('data/doc2.txt','r')
fordoc = doc1.read()
agdoc = doc2.read()
fordoc_processed = ""
agdoc_processed = ""
stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()

for word in fordoc:
    word = word.decode('utf8')
    fordoc_processed += lemmatizer.lemmatize(word)
for word in agdoc:
    word = word.decode('utf8')
    agdoc_processed += lemmatizer.lemmatize(word)

#fordoc = "the the hello"
#agdoc = "the no"

#vectorizer = CountVectorizer(ngram_range = (1,2), 
#    token_pattern = r'\b\w+\b', min_df=1, stop_words = 'english')
#counts = vectorizer.fit_transform([fordoc,agdoc])
#features = vectorizer.get_feature_names()

#transformer = TfidfTransformer() 
#tfidf = transformer.fit_transform(counts)
#print tfidf.toarray()

tf = TfidfVectorizer(ngram_range = (1,2), min_df=1, stop_words='english')
tfidf = tf.fit_transform([fordoc_processed,agdoc_processed])
features = tf.get_feature_names()

for i in range(50):
    #pdb.set_trace()
    top_results1 = [x[1] for x in sort_sparse(tfidf[0])]
    top_results2 = [x[1] for x in sort_sparse(tfidf[1])]
    print("doc1:" + features[top_results1[i]])
    print("doc2:" + features[top_results2[i]])
