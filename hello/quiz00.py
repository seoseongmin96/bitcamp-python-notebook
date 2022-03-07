import random

from hello import Member
from hello.domains import my100, myRandom, memberlist
class Quiz00:

    def quiz00calculator(self) -> float:

        num1 = myRandom(1,100)
        num2 = myRandom(1,100)
        op = ['+','-','*','/','%']
        o = myRandom(0,5)
        if op[o] == '+':
            res = num1+num2
        elif op[o] == '-':
            res = num1-num2
        elif op[o] == '*':
            res = num1*num2
        elif op[o] == '/':
            res = num1/num2
        elif op[o] == '%':
            res = num1%num2

        print(f'{num1}{op[o]}{num2}={res}')




    def quiz01bmi(self):

        name = memberlist()
        weight = myRandom(30,100)
        height = myRandom(100,200)
        bmires = weight / (height * height) * 10000
        if bmires > 25:
            res = '비만'
        elif bmires > 23:
            res = '과체중'
        elif bmires > 18.5:
            res = '정상'
        else:
            res = '저체중'
        print(f'{name}님의 {bmires: .2f}는 {res}입니다')

    def quiz02dice(self):
        print(myRandom(1,6))

    def quiz03rps(self):

        com = myRandom(0,2)
        user = myRandom(0,2)
        r = com - user
        rps = ['가위','바위','보']


        if r == 0:
            res = f' 컴퓨터 {rps[com]} 와 사용자 {rps[user]} 가 무승부'
        elif r == 1 or r == -2:
            res = f' 사용자 {rps[user]}가 컴퓨터 {rps[com]}  을 이김'
        elif r == -1 or r == 2:
            res = f' 사용자 {rps[user]}가 컴퓨터 {rps[com]}  에게 패배'
        print(f' {res}')

    def quiz04leap(self):
        i = myRandom(1000,5000)
        if (i % 4 == 0 and not i % 100 == 0 or i % 400 == 0):
            res = '윤년'
        else:
            res = '평년'
        print(f'{res}')




    def quiz05grade(self):
        name = memberlist()
        kor = myRandom(70,100)
        eng = myRandom(70,100)
        math = myRandom(70,100)
        sum = (kor + eng + math)
        avg = sum / 3
        grade = ''
        grades = ['A','B','C','D','E','F']
        if avg >= 40:
            grade = grades[9-int(avg/10)]
        elif avg == 100:
            grade = 'A+'
        else:
            grade = 'F'



        if avg <= 60:
            res = '불합격'
        else:
            res = '합격'
        print(f'{name}님의 국어 점수는 {kor}, 영어 점수는 {eng}, '
          f'수학 점수는 {math}, 총점은 {sum}, 평균 점수는 {avg: .2f},'
              f'학점은 {grade} 합격여부:{res}')


        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 65:
            return 'D'
        elif avg >= 60:
            return 'E'
        else:
            return 'F'





    def quiz06randomchoice(self):
        pass

    def chooseMember(self):
        return self.members[myRandom(0, 23)]


    def quiz07lotto(self):

        pass

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        a = Account()
        print(a.to_string())
    def quiz09gugudan(self):  # 책받침구구단

        pass


'''은행이름은 Bitbank
   입금자 이름(name), 계좌번호(account_number) , 금액(money) 속성값으로 계좌를 생성한다.
   계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성된다.
   에를 들면 123-12-123456 이다.
   금액은 100~ 999 사이로 랜덤하게 입금된다. ( 단위는 만단위로 암묵적으로 판단한다.)
'''

class Account(object):
    def __init__(self):
        self.BANK_NAME = ' 비트은행 '
        self.name = memberlist()
        a = myRandom(0, 999)
        b = myRandom(0, 99)
        c = myRandom(0, 999999)
        #self.account_number = f'{str(a).rjust(3,"0")}-{str(b).rjust(2,"0")}-{str(c).rjust(6,"0")}'
        self.account_number = self.create_account_number()
        self.money = myRandom(100, 999)





    def to_string(self):
       return f'은행 :  {self.BANK_NAME}\n ' \
              f'입금자 : {self.name}\n' \
              f'계좌번호 : {self.account_number}\n' \
              f'금액 : {self.money} 만원'



    def create_account_number(self):
        
        ls = [str(myRandom(0, 9)) for i in range(3)]
        ls.append("-")
        ls += [str(myRandom(0, 9)) for i in range(2)]
        ls.append("-")
        ls += [str(myRandom(0, 9)) for i in range(6)]


        return "".join(ls)
