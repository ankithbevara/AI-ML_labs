import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import re
from gensim.models import FastText
context = '''Modern GenAI systems are built on large language models (LLMs) like GPT, Llama, and Gemini. 
These models are trained on massive datasets using self-supervised learning and fine-tuned for specific applications such as chatbots, code generation, and content creation.
Enterprises use tools like LangChain, Hugging Face Transformers, and Prompt Engineering techniques to integrate GenAI into their workflows.
For example, marketing teams use GenAI for ad copy generation, developers use it for code assistance, and educators use it to create personalized learning materials.'''

#converting to lower case
lower = context.lower()

#some words not imp
sw = nltk.corpus.stopwords.words('english')

#word_tokenize
words = word_tokenize(lower)
for i in sw:
    if i in words:
        words.remove(i)
    word_str=' '.join(words)


#sentence tokenization
sent = sent_tokenize(word_str)
sent=''.join(sent)
spl_char = re.sub(r'[^\w\s]','',sent)

#printing words in list for vector representation
words = word_tokenize(spl_char)
print(words)
print()

#1. Converting given context into word embeddings using FastText
model = FastText(sentences=[words], #list-of-lists
                 vector_size= 50,
                 window=3,
                 min_count=1,
                 sg=1, #skipgram- 1
                 epochs=30)

#2. Analyze similarity between key terms, OUT OF VOCABULARY if not present
print("Similarity between Key terms, if not present OOV 'AI' vs 'machine':", model.wv.most_similar('ai', 'machine'))
print()
print("Similarity between Key terms, if not present OOV 'creativity' vs 'innovation':", model.wv.most_similar('creativity','innovation'))
print()
print("Similarity between Key terms, if not present OOV 'learning' vs 'training':", model.wv.most_similar('learining', 'training'))
print()
print("Similarity between Key terms, if not present OOV 'models' vs 'embeddings':", model.wv.most_similar('models','embeddings'))
print()