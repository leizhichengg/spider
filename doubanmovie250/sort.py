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
    regex_str = "<li>.*?<em\sclass=\"\">(\d{1,3})</em>.*?alt=\"(.*?)\".*?average\">(.*?)</span>"
    pattern = re.compile(regex_str, re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'title': item[1],
            'score': item[2]
        }
    return items    

def write_to_file(content):
    output = json.dumps(content, indent=4, separators=(',', ': '), ensure_ascii=False)
    with open('./sortResult.txt', 'a', encoding='UTF-8') as f:
        f.write(output)

def sort_by_score(all_results):
    all_results.sort(key = lambda k: (k.get('score', 0)), reverse = True)
    for item in all_results:
        write_to_file(item)

def main(url):
    all_results = []
    for i in range(10):
        offset = i * 25
        page_url = url + '?start=' + str(offset) + '&filter='
        html = get_one_page(page_url)
        result = parse_one_page(html)
        for item in result:
            all_results.append(item)
    sort_by_score(all_results)

if __name__ == '__main__':
    url = 'https://movie.douban.com/top250'
    main(url)