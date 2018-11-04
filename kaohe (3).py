import scrapy

class SnowstarSpider(scrapy.Spider):
    name = "snowstar"
    start_urls = ['https://snowstar.org']
    count = 0

    def parse(essay,response):
        essays = response.css("td a[targe='write']::text")
        print("len--",len(essays))
        for essay in essays:
            print("文章名"，essay.extract())
        next_page = response.css("li a[title='下一页'::attr(href)]").extract_first()
        if next_page is not None:
            essay.count<20:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page,callback=essay.parse)
