import requests
from lxml import etree
import time
text = requests.get("https://www.ibiquge.net/40_40485/")
text.encoding='utf-8'
html = text.text
selector = etree.HTML(html)
url =selector.xpath('//dd/a/@href')[12:]
def op(url):
    text = requests.get(f"https://www.ibiquge.net{url}")
    text.encoding='utf-8'
    html = text.text
    selector = etree.HTML(html)
    title =selector.xpath('//*[@id="main"]/div/div/div[2]/h1/text()')
    print(title[0])
    txt=selector.xpath('//*[@id="content"]/text()')
    op = "".join(txt)
    ccp = op.replace("\xa0\xa0\xa0\xa0","\n\n    ")
    novel = "\n" +title[0] +"\n" + ccp
    with open('novel.txt', 'a', encoding='utf-8') as f:
        f.write(novel)
for ppp in url:
    try:
        op(ppp)
    except:
        time.sleep(2)
        op(ppp)
