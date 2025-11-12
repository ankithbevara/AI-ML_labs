context = '''Innomatics Research Labs is one of the leading EdTech companies in India that focuses on skill-based learning. 
It offers training programs in Data Science, Artificial Intelligence, Machine Learning, and Full Stack Web Development. 
The curriculum is designed by industry experts and focuses on hands-on practice through projects and assignments. 

Students learn Python, SQL, Power BI, and other essential tools required for analytics and development roles. 
Every week, mentors conduct live doubt sessions to help learners clarify technical concepts. 
Innomatics provides a Learning Management System (LMS) where students can access recorded lectures, notes, and quizzes. 

Career guidance is a major part of the program. 
The placement team conducts resume workshops, mock interviews, and connects students with hiring partners from top companies. 
Many learners have successfully transitioned into data analyst, machine learning engineer, and full-stack developer roles after completing the course. 

The mentors at Innomatics are experienced professionals from the IT industry. 
They encourage students to participate in hackathons, coding challenges, and capstone projects. 
Students also get personalized mentoring sessions to strengthen their portfolios and LinkedIn profiles. 

Innomatics frequently collaborates with organizations to host guest lectures and webinars on trending topics like Generative AI, LangChain, and Prompt Engineering. 
The training focuses on real-world case studies, making learners ready for corporate challenges. 

The organization believes in the motto “Learn, Innovate, and Grow”. 
Innomatics also promotes a supportive learning culture that helps students stay motivated and confident during their learning journey. 
The LMS allows learners to track progress, complete assignments, and interact with mentors and peers. 

Students appreciate the structured course flow, dedicated support, and practical exposure they get during training. 
Overall, Innomatics Research Labs continues to bridge the gap between education and employment through its innovative teaching methods and community-driven approach.
'''
print(context)
print()

#Data Preprocessng: first we need to split data in to words(tokens)
import nltk

#converting to lower case (case-sensitive, common practice to change to lower ust incase it doesnt interpret with other words(i guess).)
lower = context.lower()
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

#printing words in List[]
words = word_tokenize(spl_char)
print(words)
print()

#converting word embeddings
from gensim.models import Word2Vec
model = Word2Vec([words],vector_size=100, window=5, min_count=1,sg=1)

similar_words = model.wv.most_similar('students','learners', topn=3)
print("Words most similar to 'students, learners':", similar_words)
print()
similar_words = model.wv.most_similar('mentors','students', topn=3)
print("Words most similar to 'mentors, teachers':", similar_words)
print()
similar_words = model.wv.most_similar('projects','assignments', topn=3)
print("Words most similar to 'projects, assignments':", similar_words)