import requests
import re
import json
import time

def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    regex_str = "<li>.*?<em\sclass=\"\">(\d{1,3})</em>.*?alt=\"(.*?)\".*?src=\"(.*?)\".*?href=\"(.*?)\".*?<p\sclass=\"\">(.*?)&nbsp;&nbsp;&nbsp;(.*?)<br>(.*?)&nbsp;.*?average\">(.*?)</span>"
    pattern = re.compile(regex_str, re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'title': item[1],
            'image': item[2],
            'link': item[3],
            'director': item[4].strip(),
            'star': item[5],
            'releasetime': item[6].strip(),
            'score': item[7]
        }

def write_to_file(content):
    output = json.dumps(content, indent=4, separators=(',', ': '), ensure_ascii=False)
    with open('./result.txt', 'a', encoding='UTF-8') as f:
        f.write(output) 

def main(offset):
    url = 'https://movie.douban.com/top250?start=' + str(offset) + '&filter='
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset = i * 25)
        time.sleep(1)