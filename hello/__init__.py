from hello.domains import Member
from hello.quiz00 import Quiz00
from hello.quiz10 import Quiz10
from hello.quiz20 import Quiz20
from hello.quiz30 import Quiz30
from hello.quiz40 import Quiz40
if __name__ == '__main__':
    q0 = Quiz00()
    q1 = Quiz10()
    q2 = Quiz20()
    q3 = Quiz30()
    q4 = Quiz40()
    while 1:
        menu = input("00계산기 01Bmi 02주사위 03가위바위보 04윤년 05성적표\n 06멤버선택 07로또 08입출금 09구구단"
                     "10버블\n 11삽입 12선택 13퀵 14병합 15매직\n 16지그재그 17소수 18골프 19예약"
                     "20리스트\n 21튜플 22딕셔너리 23컴프리 24벅스뮤직(zip) 25\n 26 27멜론 28 29DF생성"
                     "30\n 31 32 33 34 35\n 36 37 38 39 40\n 41 42 43 44 45\n 46 47 48 49")
        if menu == '00': q0.quiz00calculator()
        elif menu == '01': q0.quiz01bmi()
        elif menu == '02': q0.quiz02dice()
        elif menu == '03': q0.quiz03rps()
        elif menu == '04': q0.quiz04leap()
        elif menu == '05': q0.quiz05grade()
        elif menu == '06': q0.quiz06randomchoice()
        elif menu == '07': q0.quiz07lotto()
        elif menu == '08': q0.quiz08bank()
        elif menu == '09': q0.quiz09gugudan()
        elif menu == '10': q1.quiz10bubble()
        elif menu == '11': q1.quiz11insertion()
        elif menu == '12': q1.quiz12selection()
        elif menu == '13': q1.quiz13quick()
        elif menu == '14': q1.quiz14merge()
        elif menu == '15': q1.quiz15magic()
        elif menu == '16': q1.quiz16zigzag()
        elif menu == '17': q1.quiz17prime()
        elif menu == '18': q1.quiz18golf()
        elif menu == '19': q1.quiz19booking()
        elif menu == '20': q2.quiz20list()
        elif menu == '21': q2.quiz21tuple()
        elif menu == '22': q2.quiz22dict()
        elif menu == '23': q2.quiz23listcom()
        elif menu == '24': q2.quiz24bugs_zip()
        elif menu == '25': q2.quiz25dictcom()
        elif menu == '26': q2.quiz26map()
        elif menu == '27': q2.quiz27melon_zip()
        elif menu == '28': q2.quiz28dataframe()
        elif menu == '29': q2.quiz29_pandas_df()
        elif menu == '30': q3.quiz30_df_4_by_3()
        elif menu == '31': q3.quiz31_rand_2_by_3()
        elif menu == '32': q3.quiz32_df_grade()
        elif menu == '33': q3.quiz33_df_loc()
        elif menu == '34': q3.quiz34_df_iloc()
        elif menu == '35': q3.quiz35()
        elif menu == '36': q3.quiz36()
        elif menu == '37': q3.quiz37()
        elif menu == '38': q3.quiz38()
        elif menu == '39': q3.quiz39()
        elif menu == '40': q4.quiz40()
        elif menu == '41': q4.quiz41()
        elif menu == '42': q4.quiz42()
        elif menu == '43': q4.quiz43()
        elif menu == '44': q4.quiz44()
        elif menu == '45': q4.quiz45()
        elif menu == '46': q4.quiz46()
        elif menu == '47': q4.quiz47()
        elif menu == '48': q4.quiz48()
        elif menu == '49': q4.quiz49()
        else: break


