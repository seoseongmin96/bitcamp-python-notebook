from hello.models import Quiz01Calculator, Quiz02Bmi, Quiz03Grade, Quiz04GradeAuto, Quiz05Dice, Quiz06RandomGenerator, \
    Quiz07RandomChoice, Quiz08Rps, Quiz09GetPrime, Quiz10LeafYear ,Quiz11NumberGolf, Quiz12Lotto, Quiz13Bank,Quiz14Gugudan
from domains import Member
if __name__ == '__main__':

    while 1:
        menu = input('0.Exit 1.계산기 (+, -,*,/) 2.bmi 3.Grade 4.GradeAuto 5.Dice '
                     '6.RandomGenerator 7.RandomChoice 8. RPS 9.GetPrime 10.LeafYear'
                     '11.NumberGolf 12.Lotto 13.Bank 14.Gugudan')
        if menu == '0':
            break
        elif menu == '1':
            q1 = Quiz01Calculator(int(input('첫번째 수')), (input('계산기')), int(input('두번째 수')))
            print(f'{q1.num1} + {q1.num2} = {q1.add()}')
            print(f'{q1.num1} - {q1.num2} = {q1.sub()}')
            print(f'{q1.num1} * {q1.num2} = {q1.mul()}')
            print(f'{q1.num1} / {q1.num2} = {q1.div()}')
        elif menu == '2':
            member = Member()
            q2 = Quiz02Bmi
            member.name = input('이름 : ')
            member.height = float(input('키 : '))
            member.weight = float(input('몸무게 : '))
            res = q2.getBmi(member)
            print(f'이름: {member.name}, 키: {member.height}, '
                  f'몸무게: {member.weight}, BMI상태: {res} ')
        elif menu == '3':
            q3 = Quiz03Grade(input('이름 :'), int(input('국어 :')), int(input('영어 :')), int(input('수학')))
            print(f'이름: {q3.name}, 국어: {q3.kor}, 영어: {q3.eng}, 수학: {q3.math}, '
                  f'총합: {q3.sum()}, 평균: {q3.avg()}, 합격여부: {q3.chkPass()}')
        elif menu == '4':
            q4 = Quiz04GradeAuto()
            for i in ['김유신', '강감찬', '유관순', '윤봉길', '신사임당']:
                print(i)
            kor = int(input('국어 : '))
            eng = int(input('영어 : '))
            math = int(input('수학 : '))
            # grade =Grade(name,kor,eng,math)
            # print(f'{name}님의 국어{kor} 영어{eng} 수학{math} 합계{grade.sum()} 평균{grade.avg()}')
        elif menu == '5':
            print(Quiz05Dice.cast())

        elif menu == '6':
            q6 = Quiz06RandomGenerator
            print(q6.random())

        elif menu == '7':
            q7 = Quiz07RandomChoice()
            print(q7.chooseMember())

        elif menu == '8':
            q8 = Quiz08Rps(int(input('Player : ')))
            print(f'Player : {q8.rpsName[q8.player-1]}\n'
                  f'Com : {q8.rpsName[q8.c-1]}\n'
                  f'Res : {q8.game()}')

        elif menu == '9':
            pass

        elif menu == '10':
            q10 = Quiz10LeafYear()
            print(f'{q10.leaf()}')







