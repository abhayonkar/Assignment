import scrapy


class CompaniesSpider(scrapy.Spider):
    name = 'demo'
    
    start_urls = [
        'https://getlatka.com/saas-companies'
    ]

    def start_requests(self):
        urls = [
            'https://getlatka.com/saas-companies',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for companies in response.xpath("//table/tbody/tr"):
            yield {
                'Company': companies.xpath(".//td[2]/div/section/a/text()").extract_first(),
                'Revenue': companies.xpath(".//td[3]/p").extract_first(),
                'Funding': companies.xpath(".//td[4]/p").extract_first()
                }

        next_page = response.xpath("//div/div[2]/div/div[3]/div/a/@href").extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback = self.parse)

    
 