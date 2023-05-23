import scrapy


class myScraper(scrapy.Spider):
    start_urls = ['https://mx.investing.com/currencies/exchange-rates-table']
    name = "mycrawler"




    def parse(self, response):
        l1 = response.css("td.pid-39-last::text").extract()
        l2 = response.css("td.pid-101-last::text").extract()
        l3 = response.css("td.pid-1778-last::text").extract()
        l4 = response.css("td.pid-1901-last::text").extract()
        l5 = response.css("td.pid-1554-last::text").extract()
        l6 = response.css("td.pid-1532-last::text").extract()
        l7 = response.css("td.pid-1495-last::text").extract()

        yield {"lista[]":l1}
        yield {"lista2":l2}
        yield {"lista3": l3}
        yield {"lista4": l4}
        yield {"lista5": l5}
        yield {"lista6": l6}
        yield {"lista7": l7}

