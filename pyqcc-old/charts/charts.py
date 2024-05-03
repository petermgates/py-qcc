from ..pyqcc import Qcc

class Charts(object):
    '''
    Control chart base class. 
    '''

    def __init__(self) -> None:
        self.layers = [self]

    def __radd__(self, model):
        '''
        Layer chart objects with other passed objects.
        '''
        if isinstance(model, Qcc): # add chart to qcc base object.
            model.layers += self.layers
            return model
        self.layers.append(model) # otherwise layer chart objects.
        return self
    