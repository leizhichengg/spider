import requests
from bs4 import BeautifulSoup
import os

class meizitu():

    def __init__(self):
        self.headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

    def all_url(self, url):
        html = self.request(url)
        Soup = BeautifulSoup(html.text, 'lxml')
        all_a = Soup.find('div', class_ = 'all').find_all('a')
        all_a.pop(0)
        for a in all_a:
            title = a.get_text()
            print('Download ' + title)
            if not self.mkdir(title):
                continue
            href = a['href']
            self.html(href)
    
    def html(self, href):
        html = self.request(href)
        self.headers['Referer'] = href
        html_Soup = BeautifulSoup(html.text, 'lxml')
        max_span = html_Soup.find('div', class_ = 'pagenavi').find_all('span')[-2].get_text()
        print('Downloading...')
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url)
        print('Download over...')
    
    def img(self, page_url):
        img_html = self.request(page_url)
        img_Soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_Soup.find('div', class_ = 'main-image').find('img')['src']
        self.save(img_url)
    
    def save(self, img_url):
        name = img_url[-9:-4]
        img = self.request(img_url)
        with open(name + '.jpg', 'wb') as f:
            f.write(img.content)
            f.close()
    
    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists('/Volumes/Seagate/spiderResult/meizitu/' + path)
        if not isExists:
            print('Create path...')
            os.makedirs(os.path.join('/Volumes/Seagate/spiderResult/meizitu', path))
            os.chdir('/Volumes/Seagate/spiderResult/meizitu/' + path)
            return True
        else:
            print(path + " exists...")
            return False
    
    def request(self, url):
        content = requests.get(url, headers = self.headers)
        return content

Meizitu = meizitu()
Meizitu.all_url('https://www.mzitu.com/all/')