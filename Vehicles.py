class VehicleAbstract():

    Chassis = None
    Enginer = None
    Body    = None
    Windows = None
    Color   = None
    
    def __init__(self,*args):
        pass

    def AddEnginer(self,potencia):
        pass

    def AddBody(self,body):
        pass

    def AddChassis(self,chassis):
        pass

    def AddWindows(self,windows):
        pass

    def AddColor(self,color):
        pass

class Car(VehicleAbstract):

    def __init__(self,*args):
        print "Car is Instancead with Sucessfully!"

    def AddEnginer(self,potencia):
        self.Enginer = potencia
        print "Enginer was included in the Car"

    def AddBody(self,body):
        self.Body = body
        print "Body was included in the Car"

    def AddChassis(self,chassis):
        self.Chassis = chassis
        print "Chassis was included in the Car"

    def AddWindows(self,windows):
        self.Windows = windows
        print "Windows was included in the Car"

    def AddColor(self,color):
        self.Color = color


class Van(VehicleAbstract):

    def __init__(self,*args):
        print "Van is Instancead with Sucessfully!"

    def AddEnginer(self,potencia):
        self.Enginer = potencia
        print "Enginer was included in the Van"

    def AddBody(self,body):
        self.Body = body
        print "Body was included in the Van"

    def AddChassis(self,chassis):
        self.Chassis = chassis
        print "Chassis was included in the Van"

    def AddWindows(self,windows):
        self.Windows = windows
        print "Windows was included in the Van"

    def AddColor(self,color):
        self.Color = color


class Sedan(Car):    
    def __init__(self,*args):        

class Sporting(Car):    
    def __init__(self,*args):

class Topic(Van):
    def __init__(self,*args):
        
class Sprinter(Van):
    def __init__(self,*args):
    


def main():
    x = Car()

if(__name__=="__main__"):
    main()
