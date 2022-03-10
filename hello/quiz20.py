import random
import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen



class Quiz20:

    def quiz20list(self) -> str: return None

    def quiz21tuple(self) -> str: return None

    def quiz22dict(self) -> str: return None

    def quiz23listcom(self) -> str:
        print('-------- legacy ---------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('-------- comprehension ---------')
        a2 = [i for i in range(5)]
        print(a2)
        return None

    def quiz24zip(self) -> str:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml') # html.parser vs lxml
        '''
        # print(soup.prettify())
        artists = soup.find_all('p', {'class' : 'artist'})
        #print(type(artists)) # < class 'bs4.element.ResultSet'>
        artists = [i.get_text() for i in artists]
        #print(type(artists))
        print(''.join(i for i in artists))
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))'''
        print(self.artititle(soup, 'artist','title'))


        return None

    @staticmethod
    def artititle(soup, a, t):
        a = [i.get_text() for i in soup.find_all('p', {'class': a})]
        print(''.join(i for i in a))
        t = [i.get_text() for i in soup.find_all('p', {'class': t})]
        print(''.join(i for i in t))
        return None





    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0' }
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers = headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        #artists = soup.find_all('span',{'class' : 'checkEllipsis'})
        #artists = [i.get_text() for i in artists]
        #print('\n'.join(i for i in artists))
        title = soup.find_all('div',{'class' : 'ellipsis rank01'})
        title = [i.get_text() for i in title]
        print(''.join(i for i in title))
        #print(soup)

        return None

    def quiz28(self) -> str:
        a = [i if i == 0 or i ==0 else i for i in range()]
        b = [i if i == 0 or i ==0 else i for i in []]
        c = [(i,j) for i,j in enumerate([])]

        return None

    def quiz29(self) -> str: return None





