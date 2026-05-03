# Install if needed:
# pip install nltk contractions

import re
import nltk
import contractions
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download resources (run once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Sample text
text = "I don't like this product!!! 😡 It's very bad and disappointing."

# Step 1: Lowercasing
text = text.lower()

# Step 2: Expand contractions
text = contractions.fix(text)

# Step 3: Remove emojis and special characters
text = re.sub(r'[^a-zA-Z\s]', '', text)

# Step 4: Tokenization
tokens = word_tokenize(text)

# Step 5: Remove stopwords
stop_words = set(stopwords.words('english'))
tokens = [word for word in tokens if word not in stop_words]

# Step 6A: Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in tokens]

# Step 6B: Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]

print("Original Tokens:", tokens)
print("After Stemming:", stemmed_words)
print("After Lemmatization:", lemmatized_words)