class PlanAhorro():
    
    
    cantidadCuotasPlan = 60
    cuotasPagas = 10
        
    def __init__(self, codigoPlan, modeloVehiculo, versionVehiculo, valorVehiculo):
        self.__codigoPlan = codigoPlan
        self.__modeloVehiculo = modeloVehiculo
        self.__versionVehiculo = versionVehiculo
        self.__valorVehiculo = valorVehiculo
        self.__valorCuota = (self.getValor() / self.getCantidadCuotas()) + self.getValor() * 0.10
        
    def getCodigo(self):
        return self.__codigoPlan
    
    def getModelo(self):
        return self.__modeloVehiculo
    
    def getVersion(self):
        return self.__versionVehiculo
    
    def getValor(self):
        return self.__valorVehiculo
    
    @classmethod
    def getCantidadCuotas(cls):
        return cls.cantidadCuotasPlan
    
    @classmethod
    def getCuotasParaLicitar(cls):
        return cls.cuotasPagas
    
    def getValorCuota(self):
        return self.__valorCuota
    
    def actualizarPrecioVehiculo(self, nuevo):
        self.__valorVehiculo = nuevo
    
    def actualizarPrecioCuota(self):
        self.getValorCuota = (self.__valorVehiculo / self.__cantidadCuotasPlan) + self.__valorVehiculo * 10
    
    def __str__(self):
        return str(self.getCodigo()) + " " + str(self.getVersion()) + " " + str(self.getModelo()) + " " + str(self.getValorVehiculo()) + " " + str(self.getCantidadCuotas()) + " " + str(self.getCuotasPagas())
