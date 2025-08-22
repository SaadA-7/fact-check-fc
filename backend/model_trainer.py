import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, f1_score, classification_report
import nltk
import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import joblib
import os

# Download NLTK data
nltk.download('stopwords')
nltk.download('punkt')

class FakeNewsDetector:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=10000, stop_words='english', lowercase=True)
        self.model = LogisticRegression(random_state=42, max_iter=1000)
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))
    
    def preprocess_text(self, text):
        """Clean and preprocess text data"""
        if pd.isna(text):
            return ""
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove URLs, email addresses, and mentions
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        text = re.sub(r'\S+@\S+', '', text)
        text = re.sub(r'@\w+', '', text)
        
        # Remove punctuation and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        # Remove stopwords and stem
        words = text.split()
        words = [self.stemmer.stem(word) for word in words if word not in self.stop_words and len(word) > 2]
        
        return ' '.join(words)
    
    def train(self, true_file='True.csv', fake_file='Fake.csv'):
        """Train the fake news detection model"""
        print("Loading datasets...")
        
        # Load datasets
        try:
            true_df = pd.read_csv(true_file)
            fake_df = pd.read_csv(fake_file)
        except FileNotFoundError:
            print("CSV files not found. Creating sample data...")
            # Create sample data for demonstration
            true_df = pd.DataFrame({
                'title': ['Real soccer news title'] * 100,
                'text': ['This is real soccer news content about transfers and matches.'] * 100,
                'subject': ['soccer'] * 100,
                'date': ['2024-01-01'] * 100
            })
            fake_df = pd.DataFrame({
                'title': ['Fake soccer news title'] * 100,
                'text': ['This is fake soccer news with misleading information about players.'] * 100,
                'subject': ['soccer'] * 100,
                'date': ['2024-01-01'] * 100
            })
        
        # Add labels
        true_df['label'] = 0  # Real news
        fake_df['label'] = 1  # Fake news
        
        # Combine datasets
        df = pd.concat([true_df, fake_df], ignore_index=True)
        
        # Combine title and text for better feature extraction
        df['content'] = df['title'].fillna('') + ' ' + df['text'].fillna('')
        
        print(f"Dataset shape: {df.shape}")
        print(f"Real news articles: {len(true_df)}")
        print(f"Fake news articles: {len(fake_df)}")
        
        # Preprocess text
        print("Preprocessing text...")
        df['processed_content'] = df['content'].apply(self.preprocess_text)
        
        # Remove empty processed content
        df = df[df['processed_content'].str.len() > 0]
        
        # Split data
        X = df['processed_content']
        y = df['label']
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        print("Vectorizing text...")
        # Vectorize text
        X_train_vec = self.vectorizer.fit_transform(X_train)
        X_test_vec = self.vectorizer.transform(X_test)
        
        print("Training model...")
        # Train model
        self.model.fit(X_train_vec, y_train)
        
        # Evaluate model
        train_pred = self.model.predict(X_train_vec)
        test_pred = self.model.predict(X_test_vec)
        
        train_accuracy = accuracy_score(y_train, train_pred)
        test_accuracy = accuracy_score(y_test, test_pred)
        test_precision = precision_score(y_test, test_pred)
        test_f1 = f1_score(y_test, test_pred)
        
        print(f"\nModel Performance:")
        print(f"Training Accuracy: {train_accuracy:.4f}")
        print(f"Testing Accuracy: {test_accuracy:.4f}")
        print(f"Testing Precision: {test_precision:.4f}")
        print(f"Testing F1-Score: {test_f1:.4f}")
        
        print(f"\nClassification Report:")
        print(classification_report(y_test, test_pred, target_names=['Real', 'Fake']))
        
        return test_accuracy
    
    def predict(self, text):
        """Predict if news is fake or real"""
        processed_text = self.preprocess_text(text)
        if not processed_text:
            return {"prediction": "Real", "confidence": 0.5, "error": "Empty text after preprocessing"}
        
        text_vec = self.vectorizer.transform([processed_text])
        prediction = self.model.predict(text_vec)[0]
        probability = self.model.predict_proba(text_vec)[0]
        
        label = "Fake" if prediction == 1 else "Real"
        confidence = float(max(probability))
        
        return {
            "prediction": label,
            "confidence": confidence,
            "probabilities": {"real": float(probability[0]), "fake": float(probability[1])}
        }
    
    def save_model(self, model_path='fake_news_model.pkl', vectorizer_path='vectorizer.pkl'):
        """Save trained model and vectorizer"""
        joblib.dump(self.model, model_path)
        joblib.dump(self.vectorizer, vectorizer_path)
        print(f"Model saved to {model_path}")
        print(f"Vectorizer saved to {vectorizer_path}")
    
    def load_model(self, model_path='fake_news_model.pkl', vectorizer_path='vectorizer.pkl'):
        """Load trained model and vectorizer"""
        if os.path.exists(model_path) and os.path.exists(vectorizer_path):
            self.model = joblib.load(model_path)
            self.vectorizer = joblib.load(vectorizer_path)
            print("Model and vectorizer loaded successfully")
            return True
        return False

if __name__ == "__main__":
    detector = FakeNewsDetector()
    
    # Train the model
    accuracy = detector.train()
    
    # Save the model
    detector.save_model()
    
    # Test prediction
    sample_text = "Messi signs with Barcelona for 500 million euros per year"
    result = detector.predict(sample_text)
    print(f"\nSample prediction:")
    print(f"Text: {sample_text}")
    print(f"Prediction: {result}")