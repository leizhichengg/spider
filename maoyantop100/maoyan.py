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
    regex_str = "<dd>.*?board-index-(\d{1,3}).*?title=\"(.*?)\".*?data-src=\"(.*?)\".*?\"star\">(.*?)</p>.*?\"releasetime\">(.*?)</p>.*?score.*?\"integer\">(.*?)</i>.*?\"fraction\">(.*?)</i>"
    pattern = re.compile(regex_str, re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'title': item[1],
            'image': item[2],
            'star': item[3].strip(),
            'releasetime': item[4],
            'score': item[5] + item[6]
        }

def write_to_file(content):
    output = json.dumps(content, indent=4, separators=(',', ': '), ensure_ascii=False)
    with open('./result.txt', 'a', encoding='UTF-8') as f:
        f.write(output)

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset = i * 10)
        time.sleep(1)