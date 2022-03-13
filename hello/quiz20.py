import random
import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen
from hello.quiz00 import Quiz00
import domains
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

    def quiz24bugs_zip(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')  # html.parser vs lxml

        # self.print_music_list(soup) # 아티스트와 타이틀을 분리해서 출력하기
        # self.find_rank(soup) # 랭킹보기
        # a = [i for i in cls_names]
        # print(soup.prettify())
        ls1 = self.find_bugs_music(soup, 'title')
        ls2 = self.find_bugs_music(soup, 'artist')
        a = [i if i == 0 or i == 0 else i for i in range(1)]
        b = [i for i in []]
        c = [(i, j) for i, j in enumerate([])]
        d = {i: j for i, j in zip(ls1, ls2)}
        dict = {i:j for i, j in zip(ls1,ls2)}
        l = [ i + j for i, j in zip(ls1,ls2)]
        l2 = list(zip(ls1,ls2))
        #d1 = dict(zip(ls1,ls2))
        # self.dict1(ls1, ls2)
        # self.dict2(ls1, ls2)
        # self.dict3(ls1, ls2)
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)
        return dict

    def print_bugs_list(self, soup) -> None:
        artists = soup.find_all('p', {'class': 'artist'})
        # print(type(artists)) # <class 'bs4.element.ResultSet'>
        artists = [i.get_text() for i in artists]
        # print(type(artists))
        print(''.join(i for i in artists))
        titles = soup.find_all('p', {'class': 'title'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))

    def find_bugs_rank(self, soup):
        for i, j in enumerate(['artist', 'title']):
            for i, j in enumerate(self.find_bugs_music(soup, j)):
                print(f'{i}위 : {j}')
                print('#' * 100)

    @staticmethod
    def find_bugs_music(soup, cls_nm) -> []:
        ls = soup.find_all('p', {'class': cls_nm})
        return [i.get_text() for i in ls]



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
            dict[ls1[i]] = ls2[i]
        print(dict)

    @staticmethod
    def dict3(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)




    @staticmethod
    def quiz25dictcom() -> str:
        # memberlist()[myRandom(0,23)] 이것이 1명인데 5명 추출
        # scores 는 0~100 점 사이에서 랜덤


        q = Quiz00()
        c = set([q.quiz06randomchoice() for i in range(5)])
        while len(c) != 5:
            c.add(q.quiz06randomchoice())

        students = list(c)
        scores = [domains.myRandom(0,100) for i in range(5)]
        a = {i: j for i, j in zip(students, scores)}
        print(f'{a}')


    def quiz26map(self) -> str:
        return None

    def quiz27melon_zip(self) -> {}:

        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        ls1 = self.find_melon_music(soup,'ellipsis rank01')
        ls2 = self.find_melon_artist(soup, 'checkEllipsis')
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)
        return dict


        # artists = soup.find_all('span',{'class' : 'checkEllipsis'})
        # artists = [i.get_text() for i in artists]
        # print('\n'.join(i for i in artists))
        #title = soup.find_all('div', {'class': 'ellipsis rank01'})
        #title = [i.get_text() for i in title]
        #print(''.join(i for i in title))
        # print(soup)

    def print_melon_list(self, soup) -> None:
        for i, j in enumerate(['ellipsis rank01', 'checkEllipsis']):
            print(''.join(i for i in [i for i in self.find_melon_music(soup, j)]))
            print('*' * 100)

    def find_melon_rank(self, soup) -> None:
        for i, j in enumerate(['ellipsis rank01', 'checkEllipsis']):
            for i, j in enumerate(self.find_melon_music(soup, j)):
                print(f'{i}위 : {j}')
            print('*' * 100)

    @staticmethod
    def find_melon_music(soup, music) -> []:
        ls = soup.find_all('div', {'class': music})
        return [i.get_text() for i in ls]

    @staticmethod
    def find_melon_artist(soup, artist) -> []:
        ls = soup.find_all('span', {'class': artist})
        return [i.get_text() for i in ls]







    def quiz28dataframe(self) -> None:
       dict = self.quiz24bugs_zip()
       df = pd.DataFrame.from_dict(dict, orient = 'index')
       soup = BeautifulSoup()
       print(df)
       df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')

       dict1 = self.quiz27melon_zip()
       ds = pd.DataFrame.from_dict(dict1, orient='index')
       soup = BeautifulSoup()
       print(ds)
       ds.to_csv('./save/melon.csv', sep=',', na_rep='NaN')


       return None


    '''
        다음 결과 출력
        a   b   c
    1   1   3   5
    2   2   4   6  
    '''



    def quiz29_pandas_df(self) -> object:
        '''
        d = {'a' : [1, 2], 'b' : [3, 4], 'c' : [5, 6]} # 행렬 중 열에 해당하는 식
        df1 = pd.DataFrame(d, index=[1, 2]) # 인덱스 값 [1,2]
        d2 = {'1' : [1, 3, 5], '2' : [2, 4, 6]} # 행렬 중 행에 해당하는 식
        df2 = pd.DataFrame.from_dict(d2, orient='index',
                                     columns=['a', 'b', 'c'])  # index는 [1,2] , columns은 ['a','b','c']
        d3 = {'1' : [1, 3, 5]} # 아토믹 처리했을때의 1번째 행의 식
        d4 = {'2' : [2, 4, 6]} # 아토믹 처리했을때의 2번째 행의 식'''
        x = []
        y = []
        c = [x.append(i) if i % 2 == 0 else y.append(i) for i in range(1, 7)]
        f = [y, x]
        g = ['1', '2']
        h = {i: j for i, j in zip(g, f)}

        columns = [chr(i) for i in range(97, 100)]
        df3 = pd.DataFrame.from_dict(h, orient='index', columns=columns)

        print(df3)
        return None


'''
        a = [i if i == 0 or i ==0 else i for i in range()]
        b = [ i if i ==0 or i ==0 else i for i in []]
        c = [(i, j) for i, j in enumerate([])]
        d = ''.join([])
        e = {i:j for i, j in zip (l1, l2)}
        l = [ i + j for i, j in zip(ls1,ls2)]
        e2 = dict(zip(l1, l2))
        f = list(zip(l1, l2))
        
        a = [ i if i ==0 or i ==0 else i for i in range(1)]
        b = [ i if i ==0 or i ==0 else i for i in []]
        c = [(i,j) for i , j in enumerate([])]
        d = ''.join([])
        e = { i : j for i, j in zip(ls1,ls2)}
        f = [ i + j for i,j in zip(ls1,ls2)]
        g = dict(zip(ls1,ls2))
        h = list(zip(ls1,ls2))
'''































