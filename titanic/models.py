from icecream import ic

import titanic
from context.domains import Dataset
from context.models import Model


class TitanicModel (object):
    model = Model()
    dataset = Dataset()

        #ic(f'트레인 컬럼 {self.train.columns}')
        #ic(f'트레인 헤드 {self.train.head()}')

        # id 추출

    def preprocess(self,train_fname,test_fname):
        this = self.dataset
        that = self.model

        # 데이터셋은 Train, Test, Validation 3종류로 나뉜다
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']

        this.train = this.train.drop('Survived', axis=1)
        # Entity 에서 Object 로 전환

        this = self.drop_feature(this,'Cabin', 'Parch', 'Ticket', 'SibSp')
        #self.kwargs_sample(name='이순신')
        '''
        self.create_label(this)
       
        this = self.create_label(this)
        
        this = self.create_train(this)
        this = self.pclass_ordinal(this)
        this = self.name_nominal(this)
        this = self.sex_nominal(this)
        this = self.age_ratio(this)
        this = self.fare_ratio(this)
        this = self.embarked_nominal(this)
        '''
        self.print_this(this)
        return this


    @staticmethod
    def print_this(this):
        print('*'*100)
        ic(f'1. Train 의 타입 : {type(this.train)}\n')
        ic(f'2. Train 의 컬럼 : {(this.train.columns)}\n')
        ic(f'3. Train 의 상위 1개 : {(this.train.head(1))}\n')
        ic(f'4. Train 의 null의 개수 : {(this.train.isnull().sum())}\n')
        ic(f'5. Test 의 타입 {type(this.test)}\n')
        ic(f'6. Test 의 컬럼 {(this.test.columns)}\n')
        ic(f'7. Test 의 상위 1개 {(this.test.head(1))}\n')
        ic(f'8. Test 의 null의 개수 {(this.test.isnull().sum())}\n')
        ic(f'9. id 의 타입 : {type(this.id)}')
        ic(f'10. id의 상위 10개 :{this.id[:10]}\n')
        print('*'*100)

    @staticmethod
    def drop_feature(this, *feature) -> object:
        '''
        for i in [this.train, this.test]:
            for j in feature:
             i.drop(j,axis=1, inplace = True)'''


        [i.drop(j, axis=1, inplace = True) for j in feature  for i in [this.train, this.test]]

        '''this.train = this.train.drop('SibSp', axis=1)
        this.train = this.train.drop('Parch', axis=1)
        this.train = this.train.drop('Cabin', axis=1)
        this.train = this.train.drop('Ticket', axis=1)'''


        #this.train = [this.train.drop(i, axis=1) for i in feature]



        '''this.test = this.train.drop('SibSp', axis=1)
        this.test = this.train.drop('Parch', axis=1)
        this.test = this.train.drop('Cabin', axis=1)
        this.test = this.train.drop('Ticket', axis=1)
        this.test = [this.test.drop(i, axis=1) for i in ['Cabin', 'Parch', 'Ticket', 'Sibsp']]'''


        '''
        self.sibsp_garbage(df)
        self.parch_garbage(df)
        self.ticket_garbage(df)
        self.cabin_garbage(df)
        '''
        return this

    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        ic(type(kwargs)) #ic | type(feature) : <class 'tuple'>
        [print(''.join(f'key:{i},val:{j}')) for i,j in kwargs.items()] # key:name, val: 이순신

    def create_this(self,dataset) -> object:
        this = dataset
        this.train = self.train
        this.test = self.test
        this.id = self.id
        return this


    @staticmethod
    def create_train(this) -> object:
        return this

    '''
    Categorical vs. Quantitative
    Cate -> nominal ( 이름 ) vs. ordinal ( 순서 ) 
    Quan -> interval ( 상대 ) vs. ratio ( 절대 ) 
    '''
    @staticmethod
    def pclass_ordinal(this) -> object:
        return this
    @staticmethod
    def name_nominal(this) -> object:
        return this
    @staticmethod
    def sex_nominal(this) -> object:
        return this
    @staticmethod
    def age_ratio(this) -> object:
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        return this


