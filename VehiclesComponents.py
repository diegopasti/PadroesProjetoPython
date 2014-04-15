##############################
##                          ##
##      J A N E L A S       ##
##                          ##
##############################
class AbstractWindows():

    def __init__(self,*args):
        pass

    def getWindows(self):
        pass

class CarWindows(AbstractWindows):

    def __init__(self,*args):
        pass

    def getWindows(self,*args):
        return self


class VanWindows(AbstractWindows):

    def __init__(self,*args):
        pass

    def getWindows(self,*args):
        return self



##############################
##                          ##
##      C H A S S I S       ##
##                          ##
##############################    
class AbstractChassis():

    def __init__(self,*args):
        pass

    def getChassis(self):
        pass

class CarChassis(AbstractWindows):

    def __init__(self,*args):
        pass

    def getChassis(self,*args):
        return self


class VanChassis(AbstractWindows):

    def __init__(self,*args):
        pass

    def getChassis(self,*args):
        return self


##############################
##                          ##
##         B O D Y          ##
##                          ##
##############################    
class AbstractBody():

    def __init__(self,*args):
        pass

    def getBody(self):
        pass

class CarBody(AbstractWindows):

    def __init__(self,*args):
        pass

    def getBody(self,*args):
        return self


class VanBody(AbstractWindows):

    def __init__(self,*args):
        pass

    def getBody(self,*args):
        return self

    
