#https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
# from titanic.templates import TitanicTemp
from titanic.templates import TitanicTemp
from titanic.views import TitanicView
from titanic.models import TitanicModel
from icecream import ic
if __name__ == '__main__':
    view = TitanicView()


    while 1:

        menu = input('0.Exit 1.model 2.template')
        if menu == '0':
            break

        elif menu =='1':
            print('#### 1. model ####')
            model = TitanicModel(train_fname='train.csv',
                                 test_fname='test.csv')


        elif menu == '2':
            print('#### 2. template ####')
            temp = TitanicTemp(fname='train.csv')
            temp.visualize()
            temp.draw_survived_dead()
            break
