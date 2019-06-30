# issues
# 1. robust input
# 2. habdle bad request
# 3. use user api for further information
# 4. put all data into a dictionary and wraped it with a class

import urllib.request
import json

def getVideoInput():
    aid = input("请输入视频av号：")
    videoInfoRequest(aid)
    tagInfoRequest(aid)

def videoInfoRequest(aid):
    # request
    url = 'https://api.bilibili.com/x/web-interface/view?aid={}'.format(aid)
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    request = urllib.request.Request(url=url, headers=header)
    response = urllib.request.urlopen(request)
    dict = json.loads(response.read().decode('utf-8'))['data']
    
    # print
    print("av号："+str(dict['aid']))
    print("分P数量："+str(dict['videos']))
    print("分区id："+str(dict['tid']))
    print("分区名："+str(dict['tname']))
    print("封面图链接："+str(dict['pic']))
    print("标题："+str(dict['title']))
    print("发布时间："+str(dict['pubdate']))
    print("视频简介："+str(dict['desc']))
    print("视频总时长："+str(dict['duration']))
    
    # rights
    print('')
    print("是否电影/番剧：",end='')
    if dict['rights']['movie'] == 0:
        print("否")
    elif dict['rights']['movie'] == 1:
        print("是")
        
    print("是否需要付费：",end='')
    if dict['rights']['pay'] == 0:
        print("否")
    elif dict['rights']['pay'] == 1:
        print("是")
        
    print("是否合作视频：",end='')
    if dict['rights']['is_cooperation'] == 0:
        print("否")
    elif dict['rights']['is_cooperation'] == 1:
        print("是")
        
    print("转载信息：", end='')
    if dict['rights']['no_reprint'] == 0:
        print("默认")
    elif dict['no_reprint'] == 1:
        print("未经作者授权禁止转载")
        
    print("版权信息：", end='')
    if dict['copyright'] == 1:
        print("原创")
    elif dict['copyright'] == 2:
        print("搬运")
    
    # owner
    print('')
    print("UP主ID："+str(dict['owner']['mid']))
    print("UP主名："+str(dict['owner']['name']))
    print("UP主头像链接："+str(dict['owner']['face']))
    
    # stat
    print('')
    print("观看量："+str(dict['stat']['view']))
    print("弹幕数量："+str(dict['stat']['danmaku']))
    print("回复数量："+str(dict['stat']['reply']))
    print("收藏数量："+str(dict['stat']['favorite']))
    print("硬币数量："+str(dict['stat']['coin']))
    print("分享数量："+str(dict['stat']['share']))
    print("点赞数量："+str(dict['stat']['like']))
    print("点踩数量："+str(dict['stat']['dislike']))
    print("目前全站日排名："+str(dict['stat']['now_rank']))
    print("最高全站日排名："+str(dict['stat']['his_rank']))
    
    # pages
    print('')
    pages = dict['pages']
    for i in range(1, dict['videos']+1):
        print("第"+str(pages[i-1]['page'])+"P")
        print("  分PID："+str(pages[i-1]['cid']))
        print("  分P名："+str(pages[i-1]['part']))
        print("  分P时长："+str(pages[i-1]['duration']))
        
    # subtitle
    print('')
    print("是否允许上传字幕：", end='')
    if dict['subtitle']['allow_submit']:
        print("允许")
    else:
        print("不允许")
    print('')
    
def tagInfoRequest(aid):
    url = 'https://api.bilibili.com/x/tag/archive/tags?aid={}'.format(aid)
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    request = urllib.request.Request(url=url, headers=header)
    response = urllib.request.urlopen(request)
    dict = json.loads(response.read().decode('utf-8'))['data']
    # print
    tag_num = len(dict)
    print("标签数量："+str(tag_num))
    for i in range(tag_num):
        print("  标签id："+str(dict[i]['tag_id']))
        print("  标签名："+str(dict[i]['tag_name']))
        print("  标签封面1："+str(dict[i]['cover']))
        print("  标签封面2："+str(dict[i]['head_cover']))

getVideoInput()