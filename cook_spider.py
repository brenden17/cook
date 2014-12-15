import re

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

# from drama.items import BusItem
import scrapy

class CookItem(scrapy.Item):
    name = scrapy.Field()
    ingredients = scrapy.Field()
    recipe = scrapy.Field()

def clean(elem):
    elem = re.sub(r'\r\n', ' ', ''.join(elem).strip()) if len(elem)>0 else elem
    elem = re.sub(r'\t', ' ', elem)
    elem = re.sub(r'\n', ' ', elem)
    return re.sub(r'\((.*)\)', '', elem)

class Cookpider(CrawlSpider):
    name = "cook"
    allowed_domains = ["navercast.naver.com"]

    # start_urls = [
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=71980&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=71970&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=71955&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=71944&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=71936&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=70731&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=70728&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=70718&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=70704&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=70697&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=70114&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=70104&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=70097&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=70108&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=70103&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=70091&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=69482&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=69479&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=69477&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=69461&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=68844&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=68873&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=68830&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=68985&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=68979&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=68979&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=68975&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=68973&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=68971&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=68814&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=68811&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=66069&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=65809&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=65807&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=65805&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=65800&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=64404&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=64396&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=64367&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=64315&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=64303&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=63694&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=63741&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=63725&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=63708&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=63705&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=63687&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=63681&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=63669&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=63213&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=63213&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=63205&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=62886&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=62313&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=62306&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=62291&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=62264&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=62258&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=62267&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=62426&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=62069&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=62064&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=62038&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=62008&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=62000&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=61998&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=61992&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=61540&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=61537&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=60768&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=60759&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=60739&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=60732&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=58548&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=58544&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=58544&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=58530&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=58401&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=58396&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=58373&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=58353&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=58346&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=58012&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=57977&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=57961&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=57949&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=57941&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=57697&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=57719&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=57680&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=57661&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=57642&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=57635&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=56786&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=56780&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=56775&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=56768&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=56761&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=56755&leafId=2212",
    # "http://navercast.naver.com/magazine_contents.nhn?attrId=&contents_id=56747&leafId=2212"]

    start_urls = [
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=75647&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=75646&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=75636&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=74599&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=74591&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=74566&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=73647&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=73625&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=73590&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=71957&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=71940&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=71423&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=70788&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=70764&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=70745&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=70281&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=70275&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=70274&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=69621&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=69614&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=69346&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=69360&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=69354&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=69350&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=68678&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=68672&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=68673&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=67803&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=67778&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=67759&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=67487&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=67476&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=67458&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=66762&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=66745&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=66725&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=66065&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=66026&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=66004&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=65847&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=65838&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=65828&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=65299&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=65289&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=65286&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=64722&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=64719&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=64715&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=64049&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=64049&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=64044&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=64039&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=63324&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=63322&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=63326&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=62476&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=62455&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=62412&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=61950&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=61851&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=61819&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=61470&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=61411&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=61405&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=60758&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=60743&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=60723&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=59555&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=59505&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=59491&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=58344&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=58325&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=58318&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=58080&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=58077&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=58075&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=57624&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=57613&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=57609&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=57056&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=57053&leafId=2268",
    "http://navercast.naver.com/magazine_contents.nhn?rid=2268&attrId=&contents_id=57046&leafId=2268",
    ]


    def parse(self, response):
        ingredients = []
        name = []
        recipe = []

        for sel in response.xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/div[4]/dl/dd/ul/li/span'):
            ingredients.extend(sel.xpath('text()').extract())

        for sel in response.xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/div[5]/dl/dd/ul/li/span'):
            ingredients.extend(sel.xpath('text()').extract())

        for sel in response.xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/div[6]/dl/dd/ul/li/span'):
            ingredients.extend(sel.xpath('text()').extract())

        for sel in response.xpath('/html/body/div[1]/div[3]/div[1]/div[2]/div[2]/p'):
            recipe.extend(sel.xpath('text()').extract())

        for sel in response.xpath('/html/body/div[1]/div[2]/div[2]/div/ul/li[4]'):
            name.extend(sel.xpath('text()').extract())


            item = CookItem()
            # item['name'] = clean(''.join(name))
            # item['ingredients'] = clean(''.join(ingredients))
            item['recipe'] = clean(''.join(recipe))

            yield item
