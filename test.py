from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os

def scrape_data(url):
    # Create a Scrapy process
    process = CrawlerProcess(get_project_settings())
    name = 

    # Pass the URL as a parameter to the spider
    process.crawl(name, start_urls=[url])

    # Start the crawling process
    process.start()

    # Read the scraped data from the output file
    output_file = os.path.join('your_scrapy_project_name', 'output.json')
    with open(output_file, 'r') as f:
        result_data = f.read()

    return result_data

scrape_data("https://www.projectpro.io/article/python-libraries-for-web-scraping/625")