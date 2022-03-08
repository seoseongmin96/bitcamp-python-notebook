from hello.domains import memberlist, myRandom


class bit803:
    light = 0
    temp = 0
    def __init__(self):
        self.attend = 0
        self.name = memberlist()
        self.age = myRandom(20,30)

    def ctrl_light(self):
        pass

    def ctrl_temp(self):
        pass

    def attend(self):
        return f'이름 : {self.name}\n ' \
               f'나이 : {self.age}\n ' \
               f'출석여부 : {self.attend}'

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.움직일 대상을 선택하세요 2. 학생 정보 3. 강의실 정보')
            if menu == '0':
                break
            if menu == '1':
                pass