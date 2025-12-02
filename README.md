# AI / ML Hands-On Projects & Assignments

This repository contains my personal practice codes and mini-assignments completed for learning **Python for AI/ML**.

Each script demonstrates a core deep-learning or NLP concepts.

---

## Directory Overview

| Folder / Script | Description |
|------------------|-------------|
| **word2vec.py**, **FastText.py**, **semanticSentence.py** | Word embeddings, semantic similarity, and fast text vectorization examples |
| **AutoEncoderExample.py**, **AutoEncoderDenoising.py**, **AutoEncoderUsingSequentialModel.py** | Autoencoders for dimensionality reduction, denoising, and sequential modeling |
| **RNNTrain_LSTM.py**, **RNNTrain_GRU.py**, **NextWordPred_LSTM_Encoder_Decoder.py** | Recurrent and sequence-to-sequence models for next-word prediction |
| **arraySum.py**, **assignment1.py**, **assignment1_1.py** | Foundational Python and ML course exercises |
| **FastTextAssignment** (folder/zip) | Practice tasks using Facebook’s FastText for embeddings |
| **geminiExamples** (folder) | Multiple tasks like Role-Based, Creative Writing, MultiModular Images using gemini examples |
| **gemini_videoAssignment** (folder/zip) | Practice task of how you can extract content from a video using gemini model |
| **Streamlit** (folder/zip) | Streamlit basics to understand interactive web applications for those focused on data science, machine learning, and data visualization |
| **HuggingFace Concepts** (folder/zip) | HuggingFace inference tasks and how different models are used for different output generations |
| **autoTokenizer.ipynb** | What is AutoTokenizer? What are its properties? What is Batching, Padding, Truncation? |
---

## Topics Covered
- **Word Embeddings** – Word2Vec, FastText, Semantic Similarity  
- **Autoencoders** – Simple, Denoising, and Sequential Architectures  
- **Sequence Models** – RNN, LSTM, GRU, Encoder-Decoder  
- **Feature Representation** – Contextual vs Static embeddings  
- **General Python ML** – Data preprocessing, model evaluation, vectorization
- **Streamlit** - create functional web apps with minimal code and without requiring extensive knowledge of web development technologies.
- **HuggingFace** - A hub which is a central, community-driven platform and repository for over 2 million models, 500,000 datasets, and 1 million demos.
- **AutoTokenizers** - It acts as a smart assistant, ensuring the tokenization rules used during a model's training are applied consistently when you use that model.

---

## Tech Stack
- **Languages:** Python 3.11  
- **Libraries:** TensorFlow / Keras, PyTorch, NumPy, Pandas, Gensim, scikit-learn  
- **IDE:** VS Code / PyCharm  
- **Environment:** Virtualenv (`.venv`)

---

## Learning Goals
- Understand encoder-decoder and embedding architectures  
- Implement neural networks end-to-end using PyTorch or Keras  
- Explore contextual embeddings and vector similarity  
- Gain intuition for sequence-based models (text prediction, reconstruction)
- basic understanding of interactive web applications with streamlit

---

## How to Run
1. Clone the repository  
   ```bash
   git clone https://github.com/ankithbevara/ai-ml-labs.git
   cd ai-ml-labs

2. Create a virtual environment:
python3 -m venv .venv
source .venv/bin/activate   # (Mac/Linux)
.venv\Scripts\activate      # (Windows)

3. Install Dependencies:
pip install -r requirements.txt

4. Run any Example:
python AutoEncoderExample.py

---

## How to get a GEMINI KEY
- To run a gemini model, we need a key, to obtain:
- Go to google and search for: Google AI Studio Key
- Top right corner, click "Create API Key"
- Fill required fields like "Name your key, Project" and click "Create Key"