from context.domains import Dataset
from context.models import Model
from titanic.models import TitanicModel

from icecream import ic


class TitanicTemp (object):
    def __init__(self,train_fname, test_fname):
        self.dataset = Dataset()
        self.model = Model()
        self.titanic = TitanicModel(train_fname, test_fname)



