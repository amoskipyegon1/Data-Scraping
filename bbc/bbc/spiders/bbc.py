from urllib.parse import urljoin
import scrapy

from ..items import BbcItem


class BbcSpider(scrapy.Spider):
    name = "bbc"
    start_urls = ["http://www.bbc.com"]
    allowed_domains = ["bbc.com"]
       

    def parse(self, response):
        title_links = response.css('a.media__link::attr(href)').extract()


        for link in title_links:
            if not link.startswith('http'):
                link = urljoin(response.url, link)
                yield scrapy.Request(link, callback=self.parse_news)


    def parse_news(self, response):
        item = BbcItem()
        item['title'] = response.css('h1#main-heading::text').extract()
        if not item['title']:
            item['title'] = response.css('h1.article-headline__text.b-reith-sans-font.b-font-weight-300::text').extract()
        item['description'] = response.css('p.ssrcss-1q0x1qg-Paragraph.e1jhz7w10::text').extract()
        if not item['description']:
            item['description'] = response.xpath('//div[@class="body-text-card__text body-text-card__text--travel body-text-card__text--drop-capped body-text-card__text--flush-text"]/text()').extract()
        item['timestamp'] = response.css('time::attr(datetime)').extract()
        if not item['timestamp']:
            item['timestamp'] = response.css('span.b-font-family-serif.b-font-weight-300::text').extract()

        yield item

