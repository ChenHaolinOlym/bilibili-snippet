import urllib.request
import json
from os import system
from datetime import datetime
import csv
from time import sleep

sleep_time = 100


def requestData(aid):
    url = 'https://api.bilibili.com/x/web-interface/view?aid={}'.format(aid)
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    request = urllib.request.Request(url=url, headers=header)
    response = urllib.request.urlopen(request)
    dict = json.loads(response.read().decode('utf-8'))['data']

    return dict

def savetoCSV(dict, aid):
    with open('data--{}.csv'.format(aid), 'a+', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([dict['aid'], dict['stat']['view'],
            dict['stat']['danmaku'], dict['stat']['reply'],
            dict['stat']['favorite'], dict['stat']['coin'],
            dict['stat']['share'], dict['stat']['like'],
            dict['stat']['dislike'], dict['stat']['now_rank'],
            dict['stat']['his_rank'], datetime.now().strftime('"%Y-%m-%d %H:%M:%S"')])


aid = input('Please input the aid of the video: ')
with open('data--{}.csv'.format(aid), 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['aid', 'view', 'danmaku', 'reply', 'favorite', 'coin', 'share', 'like', 'dislike', 'now_rank', 'his_rank', 'time'])

count = 0
while True:
    savetoCSV(requestData(aid), aid)
    count += 1
    print(count)
    sleep(sleep_time)



system("pause")