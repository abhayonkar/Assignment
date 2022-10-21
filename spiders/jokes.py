from gc import callbacks
import scrapy

class JokesSpider(scrapy.Spider):
    name = 'jokes'

    start_urls = [
        'http://www.laughfactory.com/jokes/family-jokes'
    ]

    def parse(self,response):
        for joke in response.xpath("//div[@class = 'jokes']"):
            yield {
                'joke_text' : joke.xpath(".//div[@class='joke-text']/p").extract_first()
            }

# //*[@id="__next"]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]
# //*[@id="__next"]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]/p