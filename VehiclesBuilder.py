import VehiclesFactory
import Vehicles


##############################
##                          ##
##      B U I L D E R       ##
##                          ##
##############################
class VehiclesBuilderAbstract():

    def __init__(self,Car,*args):
        pass

    def BuildBody(self,*args):
        pass

    def BuildEngine(self,*args):
        pass

    def BuildChassis(self,*args):
        pass

    def BuildWindows(self,*args):
        pass

    def GetVehicle(self,*args):
        pass


class CarsBuilder(VehiclesBuilderAbstract):

    Factory = None
    ActiveVehicle = None

    def __init__(self,Car,*args):
        self.Factory = VehiclesFactory.CarsFactory()
        self.ActiveVehicle = Car
        print "Instance of Builder of Cars was Created"

    def BuildEngine(self,potencia):
        self.ActiveVehicle.AddEngine(potencia)
        print "Engine was Builded with sucessfully"

    def BuildBody(self,*args):
        self.ActiveVehicle.AddBody(self.Factory.CreateBody())
        print "Body was Builded with sucessfully"
        
    def BuildChassis(self,*args):
        self.ActiveVehicle.AddChassis(self.Factory.CreateChassis())
        print "Chassis was Builded with sucessfully"

    def BuildWindows(self,*args):
        self.ActiveVehicle.AddWindows(self.Factory.CreateWindows())
        print "Windows was Builded with sucessfully"

    def GetVehicle(self,*args):
        print "Car was builded with sucessfully"
        return self.ActiveVehicle

class VansBuilder(VehiclesBuilderAbstract):

    Factory = None
    ActiveVehicle = None
    

    def __init__(self,Car,*args):
        self.Factory = VehiclesFactory.VansFactory()
        self.ActiveVehicle = Car
        print "Instance of Builder of Cars was Created"

    def BuildEngine(self,potencia):
        self.ActiveVehicle.AddEngine(potencia)
        print "Engine was Builded with sucessfully"

    def BuildBody(self,*args):
        self.ActiveVehicle.AddBody(self.Factory.CreateBody())
        print "Body was Builded with sucessfully"
        
    def BuildChassis(self,*args):
        self.ActiveVehicle.AddChassis(self.Factory.CreateChassis())
        print "Chassis was Builded with sucessfully"

    def BuildWindows(self,*args):
        self.ActiveVehicle.AddWindows(self.Factory.CreateWindows())
        print "Windows was Builded with sucessfully"

    def GetVehicle(self,*args):
        print "Van was builded with sucessfully"
        return self.ActiveVehicle

    
##############################
##                          ##
##     D I R E C T O R      ##
##                          ##
##############################
class AbstractDirectorBuilder():

    def __init__(self,*args):
        pass

    def Build():
        pass

class CarsDirectorBuilder(AbstractDirectorBuilder):

    def __init__(self,*args):
        pass

    def Build(self,Builder):
        print "Director of construction Car instantiated successfully and began assembling the vehicle"
        Builder.BuildChassis()
        Builder.BuildEngine(Potencia)
        Builder.BuildBody()
        Builder.BuildWindows()
        Builder.GetVehicle()

class VansDirectorBuilder(AbstractDirectorBuilder):

    def __init__(self,*args):
        pass

    def Build(self,Builder,Potencia):
        print "Director of construction Vans instantiated successfully and began assembling the vehicle"
        Builder.BuildChassis()
        Builder.BuildEngine(Potencia)
        Builder.BuildBody()
        Builder.BuildWindows()
        return Builder.GetVehicle()


        
        

def main():
    veiculo = "CAR"
    if(veiculo=="CAR"):
        builder = CarsBuilder(Vehicles.Car())
        director = CarsDirectorBuilder()
        
        
    elif veiculo=="VAN":
        builder = VansBuilder(Vehicles.Van())
        director = VansDirectorBuilder()

    veiculo = director.Build(builder)

if(__name__=='__main__'):
    main()
