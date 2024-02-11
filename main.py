import asyncio
import logging
import time

from crawlers.async_crawler import AsyncCrawler
from crawlers.multithreaded_crawler import MultiThreadedCrawler
from crawlers.sync_crawler import SyncCrawler
from parsers.css_selector_parser import CssSelectorParser
from parsers.xpath_parser import XPathParser
from utils.file_sink import FileSink

def main():
    logging.basicConfig(
        format='[%(asctime)s] %(name)s %(levelname)s: %(message)s',
        datefmt='%d-%m-%y %H:%M:%S',
        level='INFO',
    )
    logger = logging.getLogger('Crawler')
    # главная - https://books.toscrape.com/index.html
    seed_urls = ['https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html']
    parser = CssSelectorParser()
    # parser = XPathParser()
    sink = FileSink('./result.jsonl')
    crawler = SyncCrawler(parser, sink, logger, seed_urls)
    # crawler = MultiThreadedCrawler(parser, sink, logger, seed_urls, max_parallel=5)
    start = time.time()
    crawler.run()
    logger.info(f'Total duration is {time.time() - start}')
    # async def run_async_crawl():
    #     crawler = AsyncCrawler(parser, sink, logger, seed_urls, rate=100, max_tries=5, max_parallel=5)
    #     start = time.time()
    #     await crawler.run()
    #     logger.info(f'Total duration is {time.time() - start}')
    # asyncio.run(run_async_crawl())

if __name__ == '__main__':
    main()