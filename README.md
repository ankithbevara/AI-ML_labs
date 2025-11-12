# AI / ML Hands-On Projects & Assignments

This repository contains my personal practice codes and mini-assignments completed while learning **Python for AI/ML**.

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

---

## Topics Covered
- **Word Embeddings** – Word2Vec, FastText, Semantic Similarity  
- **Autoencoders** – Simple, Denoising, and Sequential Architectures  
- **Sequence Models** – RNN, LSTM, GRU, Encoder-Decoder  
- **Feature Representation** – Contextual vs Static embeddings  
- **General Python ML** – Data preprocessing, model evaluation, vectorization

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