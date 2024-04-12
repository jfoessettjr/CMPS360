import scrapy

class PenguinsSpider(scrapy.Spider):
    name = 'penguins'
    start_urls = ['https://cmps360pens.netlify.app/']

    def parse(self, response):
        data_table = response.xpath('//div[@class="data"]//table')
        rows = data_table.xpath('.//tr[position()>1]')  # Skip the first row (header)
        
        for row in rows:
            name = row.xpath('.//td[1]//text()').get()
            number = row.xpath('.//td[2]//text()').get()
            position = row.xpath('.//td[3]//text()').get()
            
            yield {
                'name': name,
                'number': number,
                'position': position
            }
