import requests
from lxml import etree
import os


class Spider(object):
    def start_request(self):
        response = requests.get("https://www.qidian.com/all")
        html = etree.HTML(response.content.decode())
        book_titals = html.xpath('//div[@class = "book-mid-info"]/h4/a/text()')
        book_hrefs = html.xpath('//div[@class = "book-mid-info"]/h4/a/@href')
        for book_tital,book_href in zip(book_titals ,book_hrefs):
            # print(book_tital,book_href)
            if os.path.exists(book_tital) == False:
                os.mkdir(book_tital)
            self.file_data(book_tital,book_href)
    def file_data(self,book_tital,book_href):
        response = requests.get("https:" + book_href)
        html = etree.HTML(response.content.decode())
        tital_lists = html.xpath('//ul[@class = "cf"]/li/a/text()')
        href_lists = html.xpath('//ul[@class = "cf"]/li/a/@href')
        for tital_list,href_list in zip(tital_lists,href_lists):
            # print(tital_list,href_list)
            self.finally_file(tital_list,href_list,book_tital)
    def finally_file(self,tit,href,book_tital):
        response = requests.get("https:" + href)
        html = etree.HTML(response.content.decode())
        text_lists = html.xpath('//div[@class="read-content j_readContent"]/p/text()')
        text = "\n".join(text_lists)
        # print(text)
        file_name = book_tital + "\\" + tit + ".txt"
        print("正在抓取文章：" + file_name)
        with open(file_name,"a",encoding="utf-8") as f:
            f.write(text)

er = Spider()
er.start_request()