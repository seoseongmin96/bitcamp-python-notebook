class Calculator(object):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def add(self):
       return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

if __name__ == '__main__':
    while 1:
        menu = input('0.Exit 1.계산기 ( + , - , * , /)')
        if menu == 0:
            break
        elif menu == '1':
            num1 = int(input('첫번째 수'))
            num2 = int(input('두번째 수'))
            opcode = (input('연산 기호'))
            # 객체 생성

        print('*'*30)
        calc = Calculator(num1, num2)

        if opcode == '+':
            print(f'{calc.num1} + {calc.num2} = {calc.add()}')

        elif opcode == '-':
            print(f'{calc.num1} - {calc.num2} = {calc.sub()}')

        elif opcode == '*':
            print(f'{calc.num1} * {calc.num2} = {calc.mul()}')

        elif opcode == '/':
            print(f'{calc.num1} / {calc.num2} = {calc.div()}')

        else:
            print("Wrong Select")






