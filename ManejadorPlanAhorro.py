from ClasePlanAhorro import PlanAhorro
import csv

class ManejadorPA():
    
    def __init__(self):
        self.__lista = []
    
    def cargarPlanesCSV(self):
        archivo = open('planes.csv', 'r')
        reader = csv.reader(archivo, delimiter = ';')
        
        for fila in reader:
            plan = PlanAhorro(int(fila[0]), fila[1], fila[2], float(fila[3]))
            self.__lista.append(plan)
        archivo.close
    
    def menu(self):
        print("\n=> MENÚ <=\n")
        print("1. Mostrar archivo")
        print("2. Actualizar valor de vehiculo")
        print("3. Comparar valores")
        
    def mostrarValores(self):
        for plan in self.__lista:
            print(plan.getValor(), plan.getValorCuota())
    
    def actualizarValorVehiculo(self):
        for plan in self.__lista:
            print(f"Codigo: {plan.getCodigo()}, Modelo: {plan.getModelo()}, Version: {plan.getVersion()}")
            valor_bool = int(input("El valor es el correcto? (1-si / 2.no) "))
            if valor_bool == 1:
                print("Valor actualizado!")
            elif valor_bool == 2:
                nuevo = float(input('Ingrese el nuevo valor del vehiculo: '))
                print("Valor del vehiculo viejo: ", plan.getValor())
                plan.actualizarPrecioVehiculo(nuevo)
                print(f"Valor del vehiculo actualizado: {plan.getValor()}")
            print("\n")

    def compararCuotas(self, nueva_cuota):
        for plan in self.__lista:
            if nueva_cuota < plan.getValorCuota():
                print(plan.getCodigo(), plan.getModelo(), plan.getVersion()) 
    
    def mostrarLicito(self):
        for plan in self.__lista:
            print(f"Monto a pagar para licitar el vehiculo {plan.getModelo()} es de: ${plan.getCuotasParaLicitar() * plan.getValorCuota()}")
    
    def modificarCantidadCuotas(self, CodigoBuscado):
        i = 0
        noEncontreNada = True
        while i < len(self.__lista) and noEncontreNada:            
            if self.__lista[i].getCodigo() == CodigoBuscado:
                noEncontreNada = False
                self.__lista[i].cuotasPagas = int(input('Cantidad de cuotas para licitar nueva: '))
            else:
                i += 1
        if noEncontreNada == False:
            print('Valor cambiado con exito.')
        else:
            print('Valor NO cambiado.')
                
    def opciones(self, op):
        match op:
            case 1: 
                print(self.abrirArchivo())
            case 2:
                ManejadorPA.mostrar()
            case 3:
                nueva_cuota = float(input('Ingrese una cuota: '))
                ManejadorPA.compararCuotas(nueva_cuota)
            case _:
                print("FIN")
        
    def getActualizarValorCuota(self,nuevoV):
        valor_nuevo = ((nuevoV / PlanAhorro.__cantidadCuotasPlan) + nuevoV * 0.10)
        PlanAhorro.__valorCuota.append(valor_nuevo)
        
