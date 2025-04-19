"""
Text processing module for Persian financial content using Hazm library.
"""
from typing import List, Dict, Optional
import re
from hazm import Normalizer, Stemmer, Lemmatizer, WordTokenizer
import logging
import json
import os
from persian_tools import digits
from collections import Counter

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class FinancialTextProcessor:
    def __init__(self, custom_stopwords_path: Optional[str] = None):
        """
        Initialize the text processor with financial-specific features.
        
        Args:
            custom_stopwords_path (str, optional): Path to custom stopwords file
        """
        # Initialize Hazm components
        self.normalizer = Normalizer()
        self.stemmer = Stemmer()
        self.lemmatizer = Lemmatizer()
        self.tokenizer = WordTokenizer()
        
        # Load financial terms
        self.financial_terms = self._load_financial_terms()
        
        # Load stopwords
        self.stopwords = self._load_stopwords(custom_stopwords_path)
        
        # Set up logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename='text_processing.log'
        )
        self.logger = logging.getLogger(__name__)

    def _load_financial_terms(self) -> Dict[str, List[str]]:
        """Load financial terms and their variations."""
        financial_terms = {
            'price': ['قیمت', 'نرخ', 'ارزش', 'بها'],
            'increase': ['افزایش', 'رشد', 'صعود', 'بالا رفتن'],
            'decrease': ['کاهش', 'نزول', 'افت', 'پایین آمدن'],
            'stock': ['سهام', 'سهم', 'اوراق بهادار'],
            'market': ['بازار', 'بورس', 'تالار'],
            'company': ['شرکت', 'بنگاه', 'کارخانه'],
            'profit': ['سود', 'منفعت', 'درآمد'],
            'loss': ['زیان', 'ضرر', 'کسر'],
            'dividend': ['سود سهام', 'سود تقسیمی'],
            'volume': ['حجم', 'مقدار', 'تعداد'],
            'trade': ['معامله', 'خرید و فروش', 'مبادله'],
            'index': ['شاخص', 'نماگر', 'اندیکاتور'],
            'forecast': ['پیش‌بینی', 'تخمین', 'برآورد'],
            'analysis': ['تحلیل', 'بررسی', 'ارزیابی'],
            'report': ['گزارش', 'خلاصه', 'نتیجه']
        }
        return financial_terms

    def _load_stopwords(self, custom_path: Optional[str]) -> set:
        """Load and combine default and custom stopwords."""
        # Default Persian stopwords
        default_stopwords = set([
            'و', 'در', 'به', 'از', 'که', 'این', 'است', 'را', 'با', 'برای',
            'آن', 'یک', 'های', 'یا', 'اما', 'تا', 'هم', 'شود', 'کرد', 'شد',
            'بود', 'دارد', 'همه', 'همچنین', 'می', 'کنند', 'می‌شود', 'می‌کند'
        ])
        
        # Financial-specific stopwords to remove
        financial_stopwords = set([
            'تاریخ', 'زمان', 'ساعت', 'روز', 'ماه', 'سال', 'دقیقه',
            'ثانیه', 'هفته', 'فصل', 'دوره', 'مدت', 'زمانی'
        ])
        
        # Combine default and financial stopwords
        stopwords = default_stopwords.union(financial_stopwords)
        
        # Add custom stopwords if provided
        if custom_path and os.path.exists(custom_path):
            try:
                with open(custom_path, 'r', encoding='utf-8') as f:
                    custom_stopwords = set(json.load(f))
                stopwords.update(custom_stopwords)
            except Exception as e:
                self.logger.error(f"Error loading custom stopwords: {str(e)}")
        
        return stopwords

    def normalize_text(self, text: str) -> str:
        """
        Normalize Persian text with financial-specific rules.
        
        Args:
            text (str): Input text
            
        Returns:
            str: Normalized text
        """
        # Basic normalization
        text = self.normalizer.normalize(text)
        
        # Convert Persian numbers to English
        text = digits.convert_to_en(text)
        
        # Remove URLs
        text = re.sub(r'http\S+|www.\S+', '', text)
        
        # Remove special characters but keep financial symbols
        text = re.sub(r'[^\w\s$%+-]', ' ', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        return text

    def extract_financial_terms(self, text: str) -> List[str]:
        """
        Extract financial terms from text.
        
        Args:
            text (str): Input text
            
        Returns:
            List[str]: List of extracted financial terms
        """
        terms = []
        tokens = self.tokenizer.tokenize(text)
        
        for token in tokens:
            # Check if token is a financial term
            for category, variations in self.financial_terms.items():
                if token in variations:
                    terms.append(category)
                    break
        
        return terms

    def process_text(self, text: str) -> Dict:
        """
        Process text with all available methods.
        
        Args:
            text (str): Input text
            
        Returns:
            Dict: Processed text features
        """
        # Normalize text
        normalized = self.normalize_text(text)
        
        # Tokenize
        tokens = self.tokenizer.tokenize(normalized)
        
        # Remove stopwords
        filtered_tokens = [token for token in tokens if token not in self.stopwords]
        
        # Stem tokens
        stems = [self.stemmer.stem(token) for token in filtered_tokens]
        
        # Extract financial terms
        financial_terms = self.extract_financial_terms(normalized)
        
        # Calculate term frequencies
        term_freq = Counter(filtered_tokens)
        
        return {
            'original_text': text,
            'normalized_text': normalized,
            'tokens': filtered_tokens,
            'stems': stems,
            'financial_terms': financial_terms,
            'term_frequencies': term_freq
        }

    def batch_process(self, texts: List[str]) -> List[Dict]:
        """
        Process multiple texts in batch.
        
        Args:
            texts (List[str]): List of input texts
            
        Returns:
            List[Dict]: List of processed text features
        """
        return [self.process_text(text) for text in texts]

# Example usage:
if __name__ == "__main__":
    # Initialize processor
    processor = FinancialTextProcessor()
    
    # Example text
    text = "سهام شرکت فولاد امروز با افزایش ۲ درصدی مواجه شد و حجم معاملات به ۱۰ میلیون سهم رسید."
    
    # Process text
    result = processor.process_text(text)
    
    print("Original Text:", result['original_text'])
    print("Normalized Text:", result['normalized_text'])
    print("Financial Terms:", result['financial_terms'])
    print("Term Frequencies:", result['term_frequencies']) 
