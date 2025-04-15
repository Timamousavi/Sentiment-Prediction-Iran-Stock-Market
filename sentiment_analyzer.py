"""
Sentiment analysis model for Persian financial text.
"""
from typing import List, Dict, Tuple, Optional
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SentimentAnalyzer:
    """Sentiment analysis model for Persian financial text."""
    
    def __init__(self, model_type: str = 'logistic_regression'):
        """
        Initialize the sentiment analyzer.
        
        Args:
            model_type (str): Type of model to use ('logistic_regression', 'svm', or 'random_forest')
        """
        self.model_type = model_type
        self.vectorizer = TfidfVectorizer(
            max_features=5000,
            ngram_range=(1, 2),
            stop_words=None  # We'll handle stopwords in preprocessing
        )
        self.model = self._initialize_model()
        
    def _initialize_model(self):
        """Initialize the specified model type."""
        if self.model_type == 'logistic_regression':
            return LogisticRegression(max_iter=1000, random_state=42)
        elif self.model_type == 'svm':
            return SVC(kernel='linear', random_state=42)
        elif self.model_type == 'random_forest':
            return RandomForestClassifier(n_estimators=100, random_state=42)
        else:
            raise ValueError(f"Unknown model type: {self.model_type}")
    
    def prepare_data(self, texts: List[str], labels: List[int]) -> Tuple[np.ndarray, np.ndarray]:
        """
        Prepare data for training by vectorizing text.
        
        Args:
            texts (List[str]): List of input texts
            labels (List[int]): List of corresponding labels (0: negative, 1: positive)
            
        Returns:
            Tuple[np.ndarray, np.ndarray]: Vectorized features and labels
        """
        # Vectorize texts
        X = self.vectorizer.fit_transform(texts)
        y = np.array(labels)
        
        return X, y
    
    def train(self, texts: List[str], labels: List[int], test_size: float = 0.2):
        """
        Train the sentiment analysis model.
        
        Args:
            texts (List[str]): List of input texts
            labels (List[int]): List of corresponding labels
            test_size (float): Proportion of data to use for testing
            
        Returns:
            Dict: Training results and metrics
        """
        # Prepare data
        X, y = self.prepare_data(texts, labels)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42
        )
        
        # Train model
        logger.info(f"Training {self.model_type} model...")
        self.model.fit(X_train, y_train)
        
        # Evaluate
        train_pred = self.model.predict(X_train)
        test_pred = self.model.predict(X_test)
        
        results = {
            'train_accuracy': accuracy_score(y_train, train_pred),
            'test_accuracy': accuracy_score(y_test, test_pred),
            'train_report': classification_report(y_train, train_pred),
            'test_report': classification_report(y_test, test_pred)
        }
        
        logger.info(f"Training completed. Test accuracy: {results['test_accuracy']:.2f}")
        return results
    
    def predict(self, text: str) -> Dict:
        """
        Predict sentiment for a single text.
        
        Args:
            text (str): Input text
            
        Returns:
            Dict: Prediction results
        """
        # Vectorize text
        X = self.vectorizer.transform([text])
        
        # Predict
        prediction = self.model.predict(X)[0]
        probability = self.model.predict_proba(X)[0]
        
        return {
            'sentiment': 'positive' if prediction == 1 else 'negative',
            'confidence': float(probability[1] if prediction == 1 else probability[0])
        }
    
    def predict_batch(self, texts: List[str]) -> List[Dict]:
        """
        Predict sentiment for multiple texts.
        
        Args:
            texts (List[str]): List of input texts
            
        Returns:
            List[Dict]: List of prediction results
        """
        # Vectorize texts
        X = self.vectorizer.transform(texts)
        
        # Predict
        predictions = self.model.predict(X)
        probabilities = self.model.predict_proba(X)
        
        results = []
        for pred, prob in zip(predictions, probabilities):
            results.append({
                'sentiment': 'positive' if pred == 1 else 'negative',
                'confidence': float(prob[1] if pred == 1 else prob[0])
            })
            
        return results
    
    def save_model(self, model_path: str, vectorizer_path: str):
        """
        Save the trained model and vectorizer.
        
        Args:
            model_path (str): Path to save the model
            vectorizer_path (str): Path to save the vectorizer
        """
        joblib.dump(self.model, model_path)
        joblib.dump(self.vectorizer, vectorizer_path)
        logger.info(f"Model saved to {model_path}")
        logger.info(f"Vectorizer saved to {vectorizer_path}")
    
    @classmethod
    def load_model(cls, model_path: str, vectorizer_path: str, model_type: str = 'logistic_regression'):
        """
        Load a trained model and vectorizer.
        
        Args:
            model_path (str): Path to the saved model
            vectorizer_path (str): Path to the saved vectorizer
            model_type (str): Type of model
            
        Returns:
            SentimentAnalyzer: Loaded model instance
        """
        analyzer = cls(model_type=model_type)
        analyzer.model = joblib.load(model_path)
        analyzer.vectorizer = joblib.load(vectorizer_path)
        logger.info(f"Model loaded from {model_path}")
        return analyzer

if __name__ == "__main__":
    # Example usage
    # Sample data (in a real scenario, this would come from your dataset)
    texts = [
        "سهام شرکت فولاد امروز با افزایش قیمت مواجه شد",
        "بازار بورس امروز روند نزولی داشت",
        "تحلیل‌گران پیش‌بینی می‌کنند که این روند ادامه خواهد داشت",
        "سودآوری شرکت کاهش یافته است"
    ]
    labels = [1, 0, 1, 0]  # 1: positive, 0: negative
    
    # Initialize and train model
    analyzer = SentimentAnalyzer(model_type='logistic_regression')
    results = analyzer.train(texts, labels)
    
    # Make predictions
    test_text = "سهام شرکت فولاد امروز با افزایش قیمت مواجه شد"
    prediction = analyzer.predict(test_text)
    print(f"Prediction: {prediction}") 