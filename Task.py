class Task():
    isRunning = False
    names = [
        ['лучшие', 'лучшее', 'топ'],
        ['всё', 'всё подряд', 'all']
    ]
    filters = [
        ['сутки', 'неделя', 'месяц'],
        ['без порога', '10', '25', '50', '100']
    ]
    filters_code_names = [
        ['daily', 'weekly', 'monthly'],
        ['all', 'top10', 'top25', 'top50', 'top100']
    ]
    mySource = ''
    myFilter = ''
    def __init__(self):
        return

parser.py
import urllib.request
from bs4 import BeautifulSoup

def getTitlesFromAll(amount, rating='all'):
    output = ''
    for i in range(1, amount+1):
        try:
            if rating == 'all':
                html = urllib.request.urlopen('https://habrahabr.ru/all/page'+ str(i) +'/').read()
            else:
                html = urllib.request.urlopen('https://habrahabr.ru/all/'+ rating +'/page'+ str(i) +'/').read()
        except urllib.error.HTTPError:
            print('Error 404 Not Found')
            break
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find_all('a', class_ = 'post__title_link')
        for i in title:
            i = i.get_text()
            output += ('- "'+i+'",\n')
    return output

def getTitlesFromTop(amount, age='daily'):
    output = ''
    for i in range(1, amount+1):
        try:
            html = urllib.request.urlopen('https://habrahabr.ru/top/'+ age +'/page'+ str(i) +'/').read()
        except urllib.error.HTTPError:
            print('Error 404 Not Found')
            break
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find_all('a', class_ = 'post__title_link')
        for i in title:
            i = i.get_text()
            output += ('- "'+i+'",\n')
    return output