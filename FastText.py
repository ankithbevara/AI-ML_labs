from gensim.models import FastText
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

corpus = [["my", "name", "is", "Ankith"],
          ["her","name","is","goat"],
          ["me", "and", "her", "played", "football"],
          ["while","its","raining","heavily"],
          ["with","water","all","over","the","place"]]
print(corpus)
print()
#training fast text model

model = FastText(sentences=corpus,
                 vector_size= 50,
                 window=3,
                 min_count=1,
                 epochs=30)

#Get Vector for a word
print("Vector for 'football':", model.wv['football'])
print()
print("vector for 'goat':", model.wv['goat'])

print()

print("Similar to 'GOAT':", model.wv.most_similar('goat'))
print()
print("Similar to word 'FOOTBALL':", model.wv.most_similar('football'))
print()

#now out of vocabulary, example: there is no word "playing" in my corpus, but see we get a vector for that too!
print("Vector for 'PLAYING':",model.wv['playing'])
print()


#TRYING INFORMAL WORDS: no meanings

corpus1 = [
    ["how", "are", "you", "bro"],
    ["my", "name", "is", "ankith"],
    ["i", "am", "going", "out", "for", "dinner"],
    ["did", "you", "played", "cricket", "yesterday"],
    ["we", "went", "to", "watch", "movie", "at", "theaters"],
    ["when", "are", "you", "coming", "to", "new york"],
    ["california","has","silicon", "valley"],
    ["best","and","good","luck","for", "tomorrow"]
]

model1 = FastText(sentences=corpus1,
                  vector_size=25,
                  window=2,
                  min_count=1,
                  epochs=50)

print(model1)
print()

#getting vector
print("Vector for word 'CRICKET':", model1.wv['cricket'])
print(len(model1.wv['cricket']))
print()
#getting similar words
print("Similar words to 'SILICON':", model1.wv.most_similar('silicon'))
print()
#getting out of vocabulary
print("Vector for not existing word 'DINING':", model1.wv['dining'])
print()




#Extension of word2vector is Doc 2 Vector, instead of one word, we give one sentence in list

documents = [
    "My name is Ankith",
    "her name is goat",
    "me and she played football",
    "while its raining heavily"
    "with all over the place"    
]

#Tag each document with a unique ID
tagged_docs = [TaggedDocument(words=doc.lower().split(),
                              tags=[str(i)]) for i, doc in enumerate(documents)]

#Initialize and Train the model
model2 = Doc2Vec(vector_size=50,
                 window=2,
                 min_count=1,
                 workers=2,  #NUMBEROF CPU CORES
                 epochs=40)
model2.build_vocab(tagged_docs)
model2.train(tagged_docs, total_examples=model.corpus_count,
             epochs=model.epochs)

#getting vector for a document
print("Vector for document 0:", model2.dv['0']) #INDEX 0 = first sentence, also check its not WV its DV now
print()

#similar words
print("Most similar words for doc 1:", model2.dv['1'])
print()

#Infer vector for new unseen doc
new_doc = "My friend is in Italy"

inferred_vector = model2.infer_vector(new_doc.lower().split())
print("inferred Vector: ", inferred_vector)
print()

'''
check semanticSentence.py

from gensim.models import word2vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

#Semantic Sentence Retreival: if we give any sentence, we could be able to get similar sentence
sentences=[
    "The cat sat on the mat",
    "Dogs are loyal animals",
    "I love playing football",
    "Cats and dogs are common pets",
    "Football is a popular sport"
]

#tokenize sentences

'''