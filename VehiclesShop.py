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
        Veiculo = Vehicles.Sprinter()
        self.Director = VehiclesBuilder.VansDirectorBuilder()        
        self.Builder  = VehiclesBuilder.VansBuilder(Veiculo)
        
        if(Power == EnumCars.LOW_POWER or Power == EnumCars.MIDDLE_POWER):
            Veiculo = self.Director.Build(self.Builder)
        else:
            Veiculo = self.Director.Build(self.Builder)
            
def main():
    Shop = VanShop()
    Shop.SelectVehicle(EnumCars.MIDDLE_POWER, EnumColors.WHITE)
    

if(__name__=="__main__"):
    main()
