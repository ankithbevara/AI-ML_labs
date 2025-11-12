from gensim.models import Word2Vec

text=[["the","cat","sits","on","the","mat"],["I","am","watching","cats"],["I","am","going","to","movie"],["movie", "name", "is","mats"]]
print(text)

model = Word2Vec(text, vector_size=100, window=5, min_count=1, sg=1)

vector = model.wv['cat']
print("Vector for 'cat':", vector)
print(len(vector))

vector = model.wv['the']
print("vector for 'the':", vector)
print(len(vector))

#Finding the most similar words to "cat"
similar_words = model.wv.most_similar('cat', topn=5)
print("words most similar to 'cat':", similar_words)
print(len(similar_words))