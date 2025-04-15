"""
Text processing module for Persian financial content using Hazm library.
"""
from typing import List, Dict, Optional
import re
from hazm import Normalizer, Stemmer, Lemmatizer, WordTokenizer
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PersianTextProcessor:
    """Processor for Persian text using Hazm library."""
    
    def __init__(self):
        """Initialize the text processor with Hazm components."""
        self.normalizer = Normalizer()
        self.stemmer = Stemmer()
        self.lemmatizer = Lemmatizer()
        self.tokenizer = WordTokenizer()
        
        # Common financial terms in Persian (can be expanded)
        self.financial_terms = {
            'سهام': 'stock',
            'بورس': 'stock_market',
            'قیمت': 'price',
            'خرید': 'buy',
            'فروش': 'sell',
            'سود': 'profit',
            'زیان': 'loss',
            'تحلیل': 'analysis',
            'تکنیکال': 'technical',
            'فاندامنتال': 'fundamental'
        }
        
    def normalize_text(self, text: str) -> str:
        """
        Normalize Persian text using Hazm normalizer.
        
        Args:
            text (str): Input text to normalize
            
        Returns:
            str: Normalized text
        """
        try:
            return self.normalizer.normalize(text)
        except Exception as e:
            logger.error(f"Error normalizing text: {str(e)}")
            return text
    
    def tokenize(self, text: str) -> List[str]:
        """
        Tokenize Persian text using Hazm tokenizer.
        
        Args:
            text (str): Input text to tokenize
            
        Returns:
            List[str]: List of tokens
        """
        try:
            return self.tokenizer.tokenize(text)
        except Exception as e:
            logger.error(f"Error tokenizing text: {str(e)}")
            return text.split()
    
    def stem(self, word: str) -> str:
        """
        Stem a Persian word using Hazm stemmer.
        
        Args:
            word (str): Word to stem
            
        Returns:
            str: Stemmed word
        """
        try:
            return self.stemmer.stem(word)
        except Exception as e:
            logger.error(f"Error stemming word: {str(e)}")
            return word
    
    def lemmatize(self, word: str) -> str:
        """
        Lemmatize a Persian word using Hazm lemmatizer.
        
        Args:
            word (str): Word to lemmatize
            
        Returns:
            str: Lemmatized word
        """
        try:
            return self.lemmatizer.lemmatize(word)
        except Exception as e:
            logger.error(f"Error lemmatizing word: {str(e)}")
            return word
    
    def remove_stopwords(self, tokens: List[str]) -> List[str]:
        """
        Remove common Persian stopwords from token list.
        
        Args:
            tokens (List[str]): List of tokens
            
        Returns:
            List[str]: Filtered tokens
        """
        # Common Persian stopwords (can be expanded)
        stopwords = {
            'و', 'در', 'به', 'از', 'که', 'این', 'است', 'را', 'با', 'برای',
            'آن', 'یک', 'های', 'یا', 'اما', 'اگر', 'چون', 'چرا', 'چگونه'
        }
        
        return [token for token in tokens if token not in stopwords]
    
    def extract_financial_terms(self, text: str) -> Dict[str, int]:
        """
        Extract and count financial terms from text.
        
        Args:
            text (str): Input text
            
        Returns:
            Dict[str, int]: Dictionary of financial terms and their counts
        """
        terms_count = {term: 0 for term in self.financial_terms.keys()}
        
        for term in self.financial_terms.keys():
            # Case-insensitive search for the term
            pattern = re.compile(term, re.IGNORECASE)
            terms_count[term] = len(pattern.findall(text))
            
        return terms_count
    
    def process_text(self, text: str) -> Dict:
        """
        Process Persian text through the complete pipeline.
        
        Args:
            text (str): Input text
            
        Returns:
            Dict: Processed text features
        """
        # Normalize text
        normalized_text = self.normalize_text(text)
        
        # Tokenize
        tokens = self.tokenize(normalized_text)
        
        # Remove stopwords
        filtered_tokens = self.remove_stopwords(tokens)
        
        # Stem tokens
        stemmed_tokens = [self.stem(token) for token in filtered_tokens]
        
        # Extract financial terms
        financial_terms = self.extract_financial_terms(normalized_text)
        
        return {
            'original_text': text,
            'normalized_text': normalized_text,
            'tokens': filtered_tokens,
            'stemmed_tokens': stemmed_tokens,
            'financial_terms': financial_terms
        }

if __name__ == "__main__":
    # Example usage
    processor = PersianTextProcessor()
    sample_text = "سهام شرکت فولاد امروز با افزایش قیمت مواجه شد و تحلیل‌گران پیش‌بینی می‌کنند که این روند ادامه خواهد داشت."
    
    processed = processor.process_text(sample_text)
    print("Original Text:", processed['original_text'])
    print("Normalized Text:", processed['normalized_text'])
    print("Tokens:", processed['tokens'])
    print("Stemmed Tokens:", processed['stemmed_tokens'])
    print("Financial Terms:", processed['financial_terms']) 