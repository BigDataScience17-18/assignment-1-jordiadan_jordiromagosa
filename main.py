import scrapy
from scrapy.crawler import CrawlerProcess
from tar_spider import TarDownloader

if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(TarDownloader)
    process.crawl(TarDownloader)
    process.start() # the script will block here until the crawling is finished
