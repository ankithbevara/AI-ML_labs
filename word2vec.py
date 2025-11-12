txt = '''The sky was glowing with shades of orange and pink as the sun slowly disappeared behind the hills.  
A gentle breeze moved through the trees, carrying the scent of rain and earth.  
Birds chirped one last time before settling into their nests for the night.  
In the distance, the sound of a train echoed softly through the valley.  
Ravi stood on the balcony, sipping his tea, thinking about the journey ahead.  
He wondered how different life might be in a new city, among strangers and stories untold.  
For the first time, he felt both nervous and excited at the same moment.  
Change, he realized, wasn’t just a word — it was the beginning of something beautiful.
'''
print(txt)

#Data Preprocessng: first we need to split data in to words(tokens)
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
#nltk.download('punkt')
#nltk.download('punkt_tab')
#nltk.download('stopwords')

#converting to lower case (case-sensitive, common practice to change to lower ust incase it doesnt interpret with other words(i guess).)
lower = txt.lower()
print(lower)

print()

#some words not imp like "I, me, my, our, ours etc"
sw = nltk.corpus.stopwords.words('english')
print(sw)

print()

#word Tokenization and stopwords removal in our text data
from nltk.tokenize import word_tokenize, sent_tokenize
words = word_tokenize(lower)
for i in sw:
    if i in words:
        words.remove(i)
    word_str=' '.join(words)
print(word_str)

print()

#sentence tokenization
sent = sent_tokenize(word_str)
sent=''.join(sent)

import re
spl_char = re.sub(r'[^\w\s]','',sent)
print(spl_char)

print()

'''
words=[]
for word in spl_char:
    words.append(word_tokenize(spl_char))
print(words)

'''


words = word_tokenize(spl_char)
print(words)
print()


#Building word Embeddings
from gensim.models import Word2Vec
model = Word2Vec([words],vector_size=100, window=5, min_count=1,sg=1)

vector = model.wv['sky']
print('vector for "sky":', vector)
print(len(vector))
print()

#most similar words to 'rain'
similar_words = model.wv.most_similar('rain', topn=3)
print("Words most similar to 'village':", similar_words)
print()
similar_words = model.wv.most_similar('rain','stood', topn=3)
print("Words most similar to 'village, stood':", similar_words)