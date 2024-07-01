import scrapy


class DivanparserSpider(scrapy.Spider):
    name = "divanparser"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response): # отвечает за парсинг каждой страницы сайта поиска диванов и кресел. self - это объект класса. response - это ответ сервера поиска диванов и кресел
        divans = response.css('div._Ud0k') # ищет все div с атрибутом Ud0k (диваны и кресла) внутри div с атрибутом Ud0k (диваны и кресла) внутри div с атрибутом Ud0k (диваны и кресла)
        for divan in divans: # перебирает все div с атрибутом Ud0k (диваны и кресла) внутри div с атрибутом Ud0k (диваны и кресла)
            yield { # возвращает словарь с данными для каждого div с атрибутом Ud0k (диваны и кресла) внутри div с атрибутом Ud0k (диваны и кресла) внутри div с атрибутом Ud0k (диваны и кресла) внутри div с атрибутом Ud0k (диваны и кресла) внутри div с атрибутом Ud0k (диваны и кресла) внутри div с атрибутом Ud0k (диваны и кресла) внутри div с атрибутом Ud0k (диваны и кресла)
                'name' : divan.css("div.lsooF span::text").get(),
                'price' : divan.css("div.pY3d2 span::text").get(),
                'url' : divan.css("a").attrib['href']
            }

