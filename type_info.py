# issues
# 1. robust input
# 2. habdle bad request
# 3. use user api for further information
# 4. put all files in one package
# 5. complete the archives part
# 6. pring the tid correspond list before asking for tid

from os import system
import urllib.request
import json

class TypeInfo:
    type_url = 'http://api.bilibili.com/x/web-interface/newlist?rid={}&pn=1&ps=50'
    def __init__(self, tid):
        dict = request(self.type_url, tid)
        self.page = dict['page']
        self.archives = dict['archives']
        self.count = self.page['count']
        
    def __str__(self):
        string = '''该分类下共{}个视频
        '''.format(self.count)
        return string
        
def request(url, tid):
    url = url.format(tid)
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    request = urllib.request.Request(url=url, headers=header)
    response = urllib.request.urlopen(request)
    dict = json.loads(response.read().decode('utf-8'))['data']
    return dict


print(TypeInfo(39))





system("pause")