import random
import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


class Quiz20:

    def quiz20list(self) -> str:
        return None

    def quiz21tuple(self) -> str:
        return None

    def quiz22dict(self) -> str:
        return None

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

    def quiz24zip(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')  # html.parser vs lxml

        # self.print_music_list(soup) # 아티스트와 타이틀을 분리해서 출력하기
        # self.find_rank(soup) # 랭킹보기
        # a = [i for i in cls_names]
        # print(soup.prettify())
        ls1 = self.find_music(soup, 'title')
        ls2 = self.find_music(soup, 'artist')
        dict = {}
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        for i, j in zip(ls1, ls2):
            dict[i] = j
            print(dict)
        return dict




    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    @staticmethod
    def dict2(ls1,ls2) -> None:
        dict = {}
        for i in range(0, len(ls2)):
            dict[ls2[i]] = ls1[i]
        print(dict)

    def print_music_list(self, soup) -> None:
        artists = soup.find_all('p', {'class': 'artist'})
        # print(type(artists)) # <class 'bs4.element.ResultSet'>
        artists = [i.get_text() for i in artists]
        # print(type(artists))
        print(''.join(i for i in artists))
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_rank(self, soup):
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(self.find_music(soup, j)):
                print(f'{i}위 : {j}')
                print('#' * 100)

    @staticmethod
    def find_music(soup, cls_nm) -> []:
        ls = soup.find_all('p', {'class': cls_nm})
        return [i.get_text() for i in ls]

    def quiz25dictcom(self) -> str:
        return None

    def quiz26map(self) -> str:
        return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        # artists = soup.find_all('span',{'class' : 'checkEllipsis'})
        # artists = [i.get_text() for i in artists]
        # print('\n'.join(i for i in artists))
        title = soup.find_all('div', {'class': 'ellipsis rank01'})
        title = [i.get_text() for i in title]
        print(''.join(i for i in title))
        # print(soup)

        return None

    def quiz28dataframe(self) -> None:
       dict = self.quiz24zip()
       df = pd.DataFrame.from_dict(dict, orient = 'index')
       print(df)
       df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')

       return None

    def quiz29(self) -> str:
        '''
        a = [i if i == 0 or i == 0 else i for i in range(1)]
        b = [i for i in []]
        c = [(i, j) for i, j in enumerate([])]
        d = ''.join(i for i in [])
        return None
        '''
