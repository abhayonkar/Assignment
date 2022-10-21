import scrapy


class CompaniesSpider(scrapy.Spider):
    name = 'demo'
    
    start_urls = [
        'https://getlatka.com/saas-companies'
    ]


    def parse(self, response):
        for companies in response.xpath("//table/tbody"):
            yield {
               companies.xpath(".//tr[1]/td[2]/div/section/a").extract_first() : companies.xpath(".//tr[1]/td[3]/p").extract_first()
            }