from gensim.models import Word2Vec
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
tokenized = [sentence.lower().split() for sentence in sentences]

model = Word2Vec(sentences= tokenized,vector_size= 50, window= 3, min_count= 1,epochs=100)

#sentence embedding function
def sentence_vector(sentence, model):
    words = sentence.lower().split()
    word_vecs = [model.wv[word] for word in words if word in model.wv]
    return np.mean(word_vecs, axis=0) if word_vecs else np.zeros(model.vector_size)


#embed all sentences
sentence_embeddings = [sentence_vector(s,model) for s in sentences]

#user query

query = "I enjoy soccer"
query_vec = sentence_vector(query, model)

#compute similarity
similarities = cosine_similarity([query_vec], sentence_embeddings)[0]
best_match_index =np.argmax(similarities)

print("Query: ", query)
print()
print("Best Match", sentences[best_match_index])
print()