from hello.domains import memberlist, myRandom


class Bit803:
    light = 0
    temp = 0
    def __init__(self):
        self.attend = 0
        self.name = memberlist()
        self.age = myRandom(20,30)

    def ctrl_light(self):
        self.light = 0

    def ctrl_temp(self):
        self.temp = myRandom(0,1)

    def attend(self):
        return f'이름 : {self.name}\n ' \
               f'나이 : {self.age}\n ' \
               f'출석여부 : {self.attend}'

    @staticmethod
    def main():

        while 1:
            menu = input('0.종료 1.출석하기 /지금 출석 상태면 퇴실 2. 전등 on/off 3. 히터 on/off')
            if menu == '0':
                break
            if menu == '1':
                attend = int(input(''))


if __name__ == '__main__':
    Bit803.main()