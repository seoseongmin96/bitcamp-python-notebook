import random
import string

import numpy as np
import pandas as pd
from icecream import ic
from context.models import Model
from hello.domains import memberlist


class Quiz30:
    '''
        데이터프레임 문제 Q02
    ic| df:     A   B   C
            1   1   2   3
            2   4   5   6
            3   7   8   9
            4  10  11  12
    '''
    def quiz30_df_4_by_3(self) -> str:
        '''
        df = pd.DataFrame([[1,2,3],
                          [4,5,6],
                          [7,8,9],
                          [10,11,12]], index=range(1,5), columns=['A','B','C'])
        # 위 식을 리스트결합 형태로 분해해서 조립하시오


        ic(df)'''


        d = { '1' : range(1,4),
              '2' : range(4,7),
              '3' : range(7,10),
              '4' : range(10,13)}


        df = pd.DataFrame.from_dict(d, orient='index', columns=['A', 'B', 'C'])
        print(df)



        return None

    '''
        데이터프레임 문제 Q03.
        두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic| df:     0   1   2
                0  97  57  52
                1  56  83  80
    '''
    def quiz31_rand_2_by_3(self) -> str:
        '''
        기본 해체
        l1 = [[myRandom(0,99) for i in range(3)] for i in range(2)]
        l2 = [i for i in range(2)]
        columns = [i for i in range(3)]
        df = pd.DataFrame(l1,index=l2, columns=columns)
        '''
        # df = pd.DataFrame({},columns={})
        # 넘파이 사용한 예제
        df = pd.DataFrame(np.random.randint(10,100,size=(2,3)))
        print(df)

        return None

    '''
            데이터프레임 문제 Q04.
            국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
             단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기
             
              ic| df4:        국어  영어  수학  사회
                        lDZid  57  90  55  24
                        Rnvtg  12  66  43  11
                        ljfJt  80  33  89  10
                        ZJaje  31  28  37  34
                        OnhcI  15  28  89  19
                        claDN  69  41  66  74
                        LYawb  65  16  13  20
                        QDBCw  44  32   8  29
                        PZOTP  94  78  79  96
                        GOJKU  62  17  75  49
    '''
    @staticmethod
    def id(chr_size) -> str: return ''.join([random.choice(string.ascii_letters) for i in range(chr_size)])

    def quiz32_df_grade(self) -> str:
        col1 = ['국어', '영어', '수학', '사회']
        data1 = np.random.randint(0, 100, (10, 4))
        idx = [self.id(chr_size=5) for i in range(10)]
        df = pd.DataFrame(data1, idx, col1)
        ic(df)
        print('------------------')
        d = { i : j for i, j in zip(idx,data1)}
        df1 = pd.DataFrame.from_dict(d,orient='index',columns=col1)
        ic(df1)
        return None




    def quiz33_df_loc(self) -> str:
        '''
        d = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
             {'a': 100, 'b' : 200, 'c' : 300, 'd' : 400},
             {'a' : 1000, 'b' : 2000, 'c' : 3000, 'd' : 4000}]'''


        df = self.createDf(keys=['a','b','c','d'],
                           vals= np.random.randint(0,100,4),
                           len=3)
        # ic(df)
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
        # grade.csv





        subjects = ['자바', '파이썬', '자바스크립트', 'SQL']
        students = memberlist()
        scores = np.random.randint(0,100,(24,4))
        students_scores = {student:score for student,score in zip(students,scores)}
        students_scores_df = pd.DataFrame.from_dict(students_scores, orient="index", columns=subjects)
        model = Model()
        #model.save_model(fname='grade.csv', dframe=df)
        grade_df = model.new_model(fname='grade_backup.csv')
        ic(grade_df)
        print('Q1. 파이썬의 점수만 출력하시오')
        python_scores = grade_df.loc[:, '파이썬']
        ic(type(python_scores))
        ic(python_scores)
        print('Q2. 조현국의 점수만 출력하시오')
        cho_subjects_scores = grade_df.loc['조현국']
        ic(type(cho_subjects_scores))
        ic(cho_subjects_scores)



        # ic(df)
        return None

    @staticmethod
    def createDf(keys,vals,len):
        return pd.DataFrame([dict(zip(keys,vals)) for _ in range(len)])

    def quiz34_df_iloc(self) -> str:
        # ic(df.iloc[0])
        '''
        ic| df.iloc[0]: a    61
                b    57
                c    63
                d    19
                Name: 0, dtype: int32
        '''
        # ic(df.iloc[[0]])
        '''
        ic| df.iloc[[0]]:     a   b  c   d
                            0  36  24  2  12
        '''
        # ic(df.iloc[[0,1]])
        '''
        ic| df.iloc[[0,1]]:     a   b   c   d
                            0  27  73  90  71
                            1  27  73  90  71
        '''
        # ic(df.iloc[:3])
        '''
        ic| df.iloc[:3]:     a   b   c   d
                         0  92  28  64  62
                         1  92  28  64  62
                         2  92  28  64  62
        '''
        # ic(df.iloc[[True, False, True]])
        '''
        ic| df.iloc[[True, False, True]]:     a  b   c   d
                                          0  96  6  77  28
                                          2  96  6  77  28
        '''
        # ic(df.iloc[lambda x: x.index % 2 == 0])
        '''
        ic| df.iloc[lambda x: x.index % 2 == 0]:     a   b   c   d
                                         0  16  69  29  62
                                         2  16  69  29  62

        '''
        # ic(df.iloc[0,1])
        '''
        ic| df.iloc[0,1]: 99
        '''

        # ic(df.iloc[[0,2]],[1,3])
        '''
        ic| df.iloc[[0,2]]:     a   b   c   d
                    0  68  50  17  32
                    2  68  50  17  32
    [1,3]: [1, 3]

        '''
        # ic(df.iloc[:, [True, False, True, False]])
        '''
        ic| df.iloc[:, [True, False, True, False]]:     a   c
                                            0  52  48
                                            1  52  48
                                            2  52  48
        '''
        # ic(df.iloc[:, lambda df: [0, 2]])
        '''
        ic| df.iloc[:, lambda df: [0, 2]]:     a   c
                                   0  94  72
                                   1  94  72
                                   2  94  72
        '''

        return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None
