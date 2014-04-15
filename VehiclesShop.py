import Vehicles, VehiclesBuilder
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
    
    def __init__(self,*args):
        pass

    def SelectVehicle(self,Power,Color):        
        
        if(Power == EnumCars.LOW_POWER or Power == EnumCars.MIDDLE_POWER):
            self.Director = VehiclesBuilder.TopicDirectorBuilder()
            Veiculo = Vehicles.Topic()
        else:
            self.Director = VehiclesBuilder.SprinterDirectorBuilder()
            Veiculo = Vehicles.Sprinter()

        self.Builder  = VehiclesBuilder.VansBuilder(Veiculo)
        Veiculo = self.Director.Build(self.Builder)


class CarShop():

    Director = None
    Builder  = None
    
    def __init__(self,*args):
        pass

    def SelectVehicle(self,Power,Color):        
        
        if(Power == EnumCars.LOW_POWER or Power == EnumCars.MIDDLE_POWER):
            self.Director = VehiclesBuilder.SedanDirectorBuilder()
            Veiculo = Vehicles.Topic()
        else:
            self.Director = VehiclesBuilder.SportingDirectorBuilder()
            Veiculo = Vehicles.Sprinter()

        self.Builder  = VehiclesBuilder.VansBuilder(Veiculo)
        Veiculo = self.Director.Build(self.Builder)

        
def main():
    Shop = VanShop()
    Shop.SelectVehicle(EnumCars.HIGH_POWER, EnumColors.WHITE)

    Shop = CarShop()
    Shop.SelectVehicle(EnumCars.HIGH_POWER, EnumColors.WHITE)
    

if(__name__=="__main__"):
    main()
