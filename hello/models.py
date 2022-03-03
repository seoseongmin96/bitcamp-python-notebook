import random
class Quiz01Calculator:
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    def calc(self):
        self.add()
        self.sub()
        self.mul()
        self.div()

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2


class Quiz02Bmi:


    @staticmethod
    def getBmi(member):
        this = member
        bmires = this.weight / (this.height * this.height) * 10000
        if bmires > 25:
            return f'비만'
        elif bmires > 23:
            return f'과체중'
        elif bmires > 18.5:
            return f'정상'
        else:
            return f'저체중'


class Quiz03Grade:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3

    def getGrade(self):
        if self.avg() >= 90:
            return 'A'
        elif self.avg() >= 80:
            return 'B'
        elif self.avg() >= 70:
            return 'C'
        elif self.avg() >= 65:
            return 'D'
        elif self.avg() >= 60:
            return 'E'
        else:
            return 'F'

    def chkPass(self):  # 60점이상이면 합격
        if self.getGrade() == 'F':
            return '불합격'
        else:
            return '합격'


class Quiz04GradeAuto:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3

    def getGrade(self):
        pass

    def chkPass(self):  # 60점이상이면 합격
        pass


def myRandom(start, end):
    return random.randint(start, end)


class Quiz05Dice:
    @staticmethod
    def cast():
        return myRandom(1, 6)


class Quiz06RandomGenerator:
    def __init__(self, start, end):  # 원하는 범위의 정수에서 랜덤값 1개 추출
        self.start = start
        self.end = end

    def random(self):
        return random.randint(self.start, self.end)  # 강사님께 질문하기


class Quiz07RandomChoice:
    def __init__(self):  # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]

    def chooseMember(self):
        return self.members[myRandom(0, 23)]


class Quiz08Rps:
    def __init__(self, player):
        self.player = player
        self.rpsName = ['가위', '바위', '보']
        self.c = myRandom(1, 3)

    def game(self):
        # 1 가위 2 바위 3 보
        rps = self.player-self.c

        if rps == 0:
            res = '무승부'
        elif rps == 1 or rps == -2:
            res = '이김'
        elif rps == -1 or rps == 2:
            res = '패배'
        return res


class Quiz09GetPrime(object):
    def __init__(self):
        pass


class Quiz10LeapYear(object):
    def __init__(self):
        pass


class Quiz11NumberGolf(object):
    def __init__(self):
        pass


class Quiz12Lotto(object):
    def __init__(self):
        pass


class Quiz13Bank(object):  # 이름, 입금, 출금만 구현
    def __init__(self):
        pass


class Quiz14Gugudan(object):  # 책받침구구단
    def __init__(self):
        pass
