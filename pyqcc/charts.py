from .models import Qcc

class Chart(object):
    '''
    Control chart base class. 
    '''

    def __init__(self) -> None:
        self.layers = [self]

    def __radd__(self, model):
        '''
        Layer chart objects with other passed objects.
        '''
        if isinstance(model, Qcc): # add chart object to qcc base object.
            model.layers += self.layers
            return model
        self.layers.append(model) # otherwise append this chart object to existing.
        return self

class Imr(Chart):
    '''
    Individuals and moving range (I-MR or X-MR) control chart.
    '''
    from .constants import d2
    def __init__(self) -> None:
        super(Imr, self).__init__()
        
        # self.summary_stats()
    