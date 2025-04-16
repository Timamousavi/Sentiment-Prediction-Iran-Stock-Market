import asyncio
import schedule
import time
from datetime import datetime
import logging
from typing import List, Dict
import pandas as pd
from .scraper import FinancialContentScraper
from .telegram_scraper import TelegramScraper
import os

class DataCollectionPipeline:
    def __init__(self, 
                 telegram_api_id: int, 
                 telegram_api_hash: str,
                 financial_sites: List[str],
                 telegram_channels: List[str],
                 output_dir: str = "data/raw"):
        """
        Initialize the data collection pipeline.
        
        Args:
            telegram_api_id (int): Telegram API ID
            telegram_api_hash (str): Telegram API Hash
            financial_sites (List[str]): List of financial websites to scrape
            telegram_channels (List[str]): List of Telegram channels to monitor
            output_dir (str): Directory to save collected data
        """
        self.financial_sites = financial_sites
        self.telegram_channels = telegram_channels
        self.output_dir = output_dir
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize scrapers
        self.web_scraper = FinancialContentScraper("")  # Base URL will be set per site
        self.telegram_scraper = TelegramScraper(telegram_api_id, telegram_api_hash)
        
        # Set up logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename='data_collection.log'
        )
        self.logger = logging.getLogger(__name__)

    async def collect_web_data(self):
        """Collect data from financial websites."""
        for site in self.financial_sites:
            try:
                self.web_scraper.base_url = site
                
                # Scrape news
                news = self.web_scraper.scrape_news(page_count=3)
                news_filename = f"{self.output_dir}/{site.replace('https://', '').replace('/', '_')}_news.csv"
                self.web_scraper.save_to_csv(news, news_filename)
                
                # Scrape forum posts
                forum_posts = self.web_scraper.scrape_forum(page_count=3)
                forum_filename = f"{self.output_dir}/{site.replace('https://', '').replace('/', '_')}_forum.csv"
                self.web_scraper.save_to_csv(forum_posts, forum_filename)
                
                self.logger.info(f"Successfully collected data from {site}")
            except Exception as e:
                self.logger.error(f"Error collecting data from {site}: {str(e)}")

    async def collect_telegram_data(self):
        """Collect data from Telegram channels."""
        try:
            await self.telegram_scraper.connect()
            
            for channel in self.telegram_channels:
                messages = await self.telegram_scraper.get_channel_messages(channel, limit=100)
                filename = f"{self.output_dir}/telegram_{channel}.csv"
                self.telegram_scraper.save_to_csv(messages, filename)
                
            self.logger.info("Successfully collected data from Telegram channels")
        except Exception as e:
            self.logger.error(f"Error collecting Telegram data: {str(e)}")
        finally:
            await self.telegram_scraper.close()

    async def run_collection(self):
        """Run both web and Telegram data collection."""
        self.logger.info("Starting data collection pipeline")
        
        # Collect web data
        await self.collect_web_data()
        
        # Collect Telegram data
        await self.collect_telegram_data()
        
        self.logger.info("Data collection pipeline completed")

    def schedule_collection(self, interval_hours: int = 6):
        """
        Schedule data collection to run at regular intervals.
        
        Args:
            interval_hours (int): Interval between collections in hours
        """
        schedule.every(interval_hours).hours.do(
            lambda: asyncio.run(self.run_collection())
        )
        
        self.logger.info(f"Scheduled data collection to run every {interval_hours} hours")
        
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

# Example usage:
if __name__ == "__main__":
    # Configuration
    TELEGRAM_API_ID = YOUR_API_ID  # Replace with your API ID
    TELEGRAM_API_HASH = 'YOUR_API_HASH'  # Replace with your API Hash
    
    FINANCIAL_SITES = [
        'https://example-financial-site1.com',
        'https://example-financial-site2.com'
    ]
    
    TELEGRAM_CHANNELS = [
        'tse_ir',
        'iran_stock',
        'financial_news_ir'
    ]
    
    # Initialize and run pipeline
    pipeline = DataCollectionPipeline(
        telegram_api_id=TELEGRAM_API_ID,
        telegram_api_hash=TELEGRAM_API_HASH,
        financial_sites=FINANCIAL_SITES,
        telegram_channels=TELEGRAM_CHANNELS
    )
    
    # Run once immediately
    asyncio.run(pipeline.run_collection())
    
    # Then schedule regular collection
    pipeline.schedule_collection(interval_hours=6) 