import Vehicles, VehiclesBuilder, Clonable
class EnumCars():

    LOW_POWER    = 1300
    MIDDLE_POWER = 1800
    HIGH_POWER   = 3000

class EnumColors():

    YELLOW = "Yellow"
    WHITE = "Branco"
    BLACK = "Black"
    GRAY = "Gray"
    BLUE = "Blue"
    RED = "Red"


class VanShop():

    Director = None
    Builder  = None

    Topic    = None
    Sprinter = None
    
    def __init__(self,*args):
        pass

    def SelectVehicle(self,Power,Color):        
        
        if(Power == EnumCars.LOW_POWER or Power == EnumCars.MIDDLE_POWER):
            self.Director = VehiclesBuilder.TopicDirectorBuilder()
            self.Builder  = VehiclesBuilder.VansBuilder(Vehicles.Topic())
            if(self.Topic == None):
                self.Topic = self.Director.Build(self.Builder)
                Veiculo = self.Topic
            else:
                Veiculo = self.Topic.Clone()
        else:
            self.Director = VehiclesBuilder.SprinterDirectorBuilder()
            self.Builder  = VehiclesBuilder.VansBuilder(Vehicles.Sprinter())
            if(self.Sprinter == None):
                self.Sprinter = self.Director.Build(self.Builder)
                Veiculo = self.Sprinter
            else:
                Veiculo = self.Sprinter.Clone()
                
        return Veiculo


class CarShop():

    Director = None
    Builder  = None

    Sedan    = None
    Sporting = None
    
    
    def __init__(self,*args):
        pass

    def SelectVehicle(self,Power,Color):        
        
        if(Power == EnumCars.LOW_POWER or Power == EnumCars.MIDDLE_POWER):
            self.Director = VehiclesBuilder.SedanDirectorBuilder()
            self.Builder  = VehiclesBuilder.CarsBuilder(Vehicles.Sedan())
            if(self.Sedan == None):
                self.Sedan = self.Director.Build(self.Builder)
                Veiculo = self.Sedan
            else:
                Veiculo = self.Sedan.Clone()
            
        else:
            self.Director = VehiclesBuilder.SportingDirectorBuilder()
            self.Builder  = VehiclesBuilder.CarsBuilder(Vehicles.Sporting())
            if(self.Sporting == None):
                self.Sporting = self.Director.Build(self.Builder)
                Veiculo = self.Sporting
            else:
                Veiculo = self.Sporting.Clone()

        return Veiculo

        
def main():
    Shop = VanShop()
    Shop.SelectVehicle(EnumCars.HIGH_POWER, EnumColors.WHITE)

    Shop.SelectVehicle(EnumCars.HIGH_POWER, EnumColors.WHITE)

    Shop.SelectVehicle(EnumCars.HIGH_POWER, EnumColors.WHITE)

    Shop = CarShop()
    Shop.SelectVehicle(EnumCars.HIGH_POWER, EnumColors.WHITE)
    Shop.SelectVehicle(EnumCars.HIGH_POWER, EnumColors.WHITE)
    

if(__name__=="__main__"):
    main()
