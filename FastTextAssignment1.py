import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import re
from gensim.models import FastText

context = '''Generative AI (GenAI) represents one of the most transformative areas in artificial intelligence, focusing on the ability of machines to create new content such as text, images, audio, and video.
 Companies across industries are rapidly adopting GenAI to automate creative processes, enhance productivity, and personalize user experiences.
Modern GenAI systems are built on large language models (LLMs) like GPT, Llama, and Gemini.
 These models are trained on massive datasets using self-supervised learning and fine-tuned for specific applications such as chatbots, code generation, and content creation.
Enterprises use tools like LangChain, Hugging Face Transformers, and Prompt Engineering techniques to integrate GenAI into their workflows.
 For example, marketing teams use GenAI for ad copy generation, developers use it for code assistance, and educators use it to create personalized learning materials.
Training data quality, tokenization, embeddings, and model architecture play a critical role in determining the quality of generated outputs.
 To improve accuracy, researchers employ vector databases, retrieval-augmented generation (RAG), and fine-tuning pipelines to make AI systems more context-aware.
GenAI has also influenced fields like design, healthcare, and education by enabling faster idea generation and adaptive feedback systems.
 Ethical AI and bias mitigation remain major focus areas to ensure responsible AI development.
Overall, Generative AI continues to redefine creativity and innovation by bridging the gap between human imagination and machine intelligence.
'''

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

#2. Analyze similarity between key terms 
print("Similarity between Key terms 'AI' vs 'machine':", model.wv.most_similar('ai', 'machine'))
print()
print("Similarity between Key terms 'creativity' vs 'innovation':", model.wv.most_similar('creativity','innovation'))
print()
print("Similarity between Key terms 'learning' vs 'training':", model.wv.most_similar('learining', 'training'))
print()
print("Similarity between Key terms 'models' vs 'embeddings':", model.wv.most_similar('models','embeddings'))
print()