# 🚀 NLP Foundations

> A structured, beginner-to-intermediate guide to **Natural Language Processing (NLP)** — from text cleaning to machine learning models.

---

## 🧠 What is NLP?

**Natural Language Processing (NLP)** is a field of Artificial Intelligence that enables machines to:

* 📖 Understand human language
* 🧠 Interpret meaning
* 💬 Generate responses

---

## 🌍 Real-World Applications

* 🔍 Search Engines (Google)
* 🤖 Chatbots (ChatGPT)
* 😊 Sentiment Analysis (reviews, feedback)
* 🌐 Machine Translation (Google Translate)
* 📧 Spam Detection

---

## ⚙️ NLP Pipeline (High-Level)

```text
Raw Text → Preprocessing → Feature Engineering → Model → Output
```

---

## 📚 1. Introduction to NLP

### 🔹 Key Concepts

* **Natural Language Understanding (NLU)** → Understanding text
* **Natural Language Generation (NLG)** → Generating text

---

### 🔹 NLP Pipeline

```text
Data Collection
     ↓
Text Cleaning
     ↓
Feature Engineering
     ↓
Model Training
     ↓
Evaluation
```

---

## 🧹 2. Text Preprocessing & Cleaning

> Cleaning text is the **most important step** in NLP

---

### 🔹 Tokenization

Breaking text into words or sentences

```python
"I love NLP" → ["I", "love", "NLP"]
```

---

### 🔹 Normalization

#### ✂️ Stemming

```text
playing → play  
studies → studi ❌
```

#### 📚 Lemmatization

```text
studies → study ✅  
better → good ✅
```

---

### 🔹 Stop Word Removal

Removing common words:

```text
"I am going to the store"
→ ["going", "store"]
```

---

### 🔹 Regular Expressions (Regex)

Pattern-based text cleaning:

```python
import re
text = re.sub(r'[^a-zA-Z]', '', text)
```

---

### 🔹 Handling Noisy Data

* Remove punctuation
* Remove special characters
* Expand contractions ("don't" → "do not")
* Convert to lowercase

---

## 🧮 3. Text Representation & Feature Engineering

> Machines understand **numbers**, not text

---

### 🔹 Bag of Words (BoW)

Counts word frequency

```text
"I love NLP" → {I:1, love:1, NLP:1}
```

---

### 🔹 TF-IDF

Weighs words by importance

* Common words → low weight
* Rare important words → high weight

---

### 🔹 N-Grams

Captures word sequences:

* Unigram → "I", "love"
* Bigram → "I love"
* Trigram → "I love NLP"

---

### 🔹 Word Embeddings

Dense vector representations:

* Word2Vec
* GloVe
* FastText

---

## 🤖 4. Classical NLP Techniques & ML Models

---

### 🔹 Part-of-Speech (POS) Tagging

Identify grammar:

```text
"I love NLP"
→ I (Pronoun), love (Verb), NLP (Noun)
```

---

### 🔹 Named Entity Recognition (NER)

Extract entities:

```text
"Elon Musk founded SpaceX"
→ Person: Elon Musk
→ Organization: SpaceX
```

---

### 🔹 Text Classification

Used for:

* Sentiment Analysis
* Spam Detection

Models:

* Naive Bayes
* Logistic Regression
* Support Vector Machines (SVM)

---

### 🔹 Topic Modeling

Discover hidden topics in text:

* Latent Dirichlet Allocation (LDA)

---

## 🧠 Final Mental Model

```text
Text → Clean → Convert → Learn → Predict
```

---

## 🎯 Why This Matters

If you're a **Data Engineer / AI Engineer**, NLP is used in:

* 📊 Log analysis
* 🏥 Healthcare text processing
* 🤖 Chatbots
* 📄 Document processing
* 🔍 Search & recommendation systems

---

## 📌 Author

**Ravi Kumar**
Data & AI Engineer

---

> 💡 *"Better preprocessing = Better models"*
