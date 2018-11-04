import  scrapy

class  Snowstar(scrapy.Spider):
    name = "snoestar"
    allowed_domains = ["snowstar.org"]
    start_urls = ["https://snowstar.org"]


    def parse(self,response):
        filename = response.url.spilt("/")[-2]

        with open(filename,'wb') as f:
            f.write(response.body)
