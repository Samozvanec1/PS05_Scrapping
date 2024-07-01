import scrapy


class DzlightSpider(scrapy.Spider):
    name = "DZlight"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):  # этот метод отвечает за парсинг каждой страницы сайта поиска светильников. self - это объект класса. response - это ответ сервера поиска светильников
        lamps = response.css('div._Ud0k') #этот метод ищет все div с атрибутом Ud0k (диваны и кресла) внутри div с атрибутом Ud0k (диваны и кресла)
        for lamp in lamps: # перебирает все div с атрибутом Ud0k (диваны и кресла) внутри div с атрибутом Ud0k (диваны и кресла)
            yield {
                'name': lamp.css("div.lsooF span::text").get(), # ищет все div с атрибутом lsooF (название) внутри div с атрибутом lsooF (название)
                'price': lamp.css("div.pY3d2 span::text").get(),
                'url': lamp.css("a").attrib['href']
            }
