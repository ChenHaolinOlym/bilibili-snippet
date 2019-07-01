# issues
# 1. robust input
# 2. habdle bad request
# 3. use user api for further information
# 4. put all files in one package


import urllib.request
import json
from os import system

class ArticleInfo:
    article_url = 'https://api.bilibili.com/x/article/viewinfo?id={}'
    def __init__(self, cid):
        dict = request(self.article_url, cid)
        self.dict = dict
        self.cv = cid
        self.outer_like = dict['like']
        self.outer_attention = dict['attention']
        self.outer_favorite = dict['favorite']
        self.outer_coin = dict['coin']
        self.view = dict['stats']['view']
        self.favorite = dict['stats']['favorite']
        self.like = dict['stats']['like']
        self.dislike = dict['stats']['dislike']
        self.reply = dict['stats']['reply']
        self.share = dict['stats']['share']
        self.coin = dict['stats']['coin']
        self.title = dict['title']
        self.banner_url = dict['banner_url']
        self.author_id = dict['mid']
        self.author_name = dict['mid']
        self.image_urls = dict['image_urls'][0]
        self.origin_image_urls = dict['origin_image_urls'][0]
        self.shareable = dict['shareable']
        self.show_later_watch = dict['show_later_watch']
        self.show_small_window = dict['show_small_window']
        self.in_list = dict['in_list']
        self.pre = dict['pre']
        self.next = dict['next']
        
        
def request(url, cid):
    url = url.format(cid)
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    request = urllib.request.Request(url=url, headers=header)
    response = urllib.request.urlopen(request)
    dict = json.loads(response.read().decode('utf-8'))['data']
    return dict


a = ArticleInfo(2)
print(a.cv)



system("pause")