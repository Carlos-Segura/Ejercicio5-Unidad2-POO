from ManejadorPlanAhorro import ManejadorPA             

if __name__ == '__main__':
    manejador = ManejadorPA()
    manejador.cargarPlanesCSV()
    manejador.mostrarValores()
    # manejador.menu()
    # op = int(input('Ingrese una opcion: '))
    # while op != 0:
    #     manejador.opciones(op)
    #     op = int(input('\nIngrese una opcion: '))
    manejador.actualizarValorVehiculo()
    manejador.mostrarValores()
    manejador.mostrarLicito()
    CodigoBuscado = int(input('Ingrese un codigo a buscar: '))
    manejador.modificarCantidadCuotas(CodigoBuscado)