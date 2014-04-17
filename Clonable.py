class Clonable(object):

    def __init__(self,*args):
        pass

    def Clone(self,*args):
        import copy
        print self," esta sendo clonado"
        return copy.deepcopy(self)
