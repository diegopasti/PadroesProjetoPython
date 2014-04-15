import VehiclesComponents

class VehiclesFactoryAbstract():

    def __init__(self,*args):
        pass

    def CreateBody():
        pass

    def CreateChassis():
        pass

    def CreateWindows():
        pass

class VansFactory(VehiclesFactoryAbstract):

    def __init__(self,*args):
        print "Instance of Factory of Vans was Created"

    def CreateBody(self):
        print "Body of Van was created with sucessfuly"
        return VehiclesComponents.VanBody().getBody()

    def CreateChassis(self):
        print "Chassis of Van was created with sucessfuly"
        return VehiclesComponents.VanChassis().getChassis()

    def CreateWindows(self,*args):
        print "Windows of Van was created with sucessfuly"
        return VehiclesComponents.VanWindows().getWindows()


class CarsFactory(VehiclesFactoryAbstract):

    def __init__(self,*args):
        print "Instance of Factory of Cars was Created"

    def CreateBody(self):
        print "Body of Car was created with sucessfuly"
        return VehiclesComponents.CarBody().getBody()

    def CreateChassis(self):
        print "Chassis of Car was created with sucessfuly"
        return VehiclesComponents.CarChassis().getChassis()

    def CreateWindows(self,*args):
        print "Windows of Car was created with sucessfuly"
        return VehiclesComponents.CarWindows().getWindows()



def main():
    veiculo = "CARRO"
    if(veiculo=="CARRO"):
        x = CarsFactory()
    elif veiculo=="VAN":
        x = VansFactory()

    x.CreateWindows()
    x.CreateChassis()
    x.CreateBody()

if __name__ == "__main__":
    main()




