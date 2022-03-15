from icecream import ic

from context.domains import Dataset
from context.models import Model


class TitanicModel (object):
    def __init__(self, train_fname, test_fname):
        self.model = Model()
        self.dataset = Dataset()
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        # id 추출

        ic(f'트레인 컬럼 {self.train.columns}')
        ic(f'트레인 헤드 {self.train.head()}')
        ic(self.train)


    def preprocess(self):
        self.sib_sp_garbage()
        self.parch_garbage()
        self.ticket_garbage()
        self.cabin_garbage()
        self.create_label()
        self.create_label()
        self.pclass_ordinal()
        self.name_nominal()
        self.sex_nominal()
        self.age_ratio()
        self.fare_ratio()
        self.embarked_nominal()



    def create_label(self):
        pass

    def create_train(self) -> object:
        pass

    def drop_feature(self) -> object:
        pass

    '''
    Categorical vs. Quantitative
    Cate -> nominal ( 이름 ) vs. ordinal ( 순서 ) 
    Quan -> interval ( 상대 ) vs. ratio ( 절대 ) 
    '''

    def pclass_ordinal(self) -> object:
        pass

    def name_nominal(self) -> object:
        pass

    def sex_nominal(self) -> object:
        pass

    def age_ratio(self) -> object:
        pass

    def sib_sp_garbage(self) -> object:
        self.drop_feature()

    def parch_garbage(self) -> object:
        self.drop_feature()

    def ticket_garbage(self) -> object:
        pass

    def fare_ratio(self) -> object:
        pass

    def cabin_garbage(self) -> object:
        pass

    def embarked_nominal(self) -> object:
        pass


