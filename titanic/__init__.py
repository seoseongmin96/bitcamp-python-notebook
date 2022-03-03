#https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from titanic.views import View

if __name__ == '__main__':
    def print_menu():

        print('1.전처리')


    view = View()
    while 1:

        menu = input(print_menu())
        if menu == '1':
            print(' #### 1. 전처리 ####')
            view.preprocess('train.csv','test.csv')
        else:
         break
