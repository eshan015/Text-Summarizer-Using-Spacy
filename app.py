from flask import Flask, render_template, request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
from text_summary import summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        url = request.form['url']
        result_data = scrape_data(url)
        return render_template('result.html', result_data=result_data)
    
def scrape_data(url):
    # Create a Scrapy process
    process = CrawlerProcess(get_project_settings())

    # Pass the URL as a parameter to the spider
    process.crawl('your_spider_name', start_urls=[url])

    # Start the crawling process
    process.start()

    # Read the scraped data from the output file
    output_file = os.path.join('your_scrapy_project_name', 'output.json')
    with open(output_file, 'r') as f:
        result_data = f.read()

    return result_data
    

        # summary, original_txt, len_original_txt, len_summary = summarizer(rawtext)
        # return render_template('summary.html', summary = summary, original_txt = original_txt, len_original_txt = len_original_txt, len_summary = len_summary)

if __name__ == "__main__":
    app.run(debug=True)