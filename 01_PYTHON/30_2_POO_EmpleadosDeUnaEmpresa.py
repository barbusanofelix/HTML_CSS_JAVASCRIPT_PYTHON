

'''
La clase empleado contiene los datos que serán compartidos por sus clases hijas. La clase empleado contiene un constructor para
inicializar sus atributos.
Los datos utilizados son: nombre completo, cedula y teléfono. Cada atributo de la clase cuenta con sus respectivos get y set.
'''
class Empleado():
    #Atributos
    __nombreCompleto:str
    __cedula:str
    __telefono:int
        
    #Constructor Empleados
    def __init__(self,nombreCompleto, cedula, telefono):
        self.__nombreCompleto=nombreCompleto
        self.__cedula =cedula
        self.__telefono=telefono
        
    #* GET - SET __nombreCompleto    
    def get__nombreCompleto(self):
        return self.__nombreCompleto
    def set__nombreCompleto(self,nombreCompleto):
        self.__nombreCompleto=nombreCompleto
    
    #* GET - SET __cedula    
    def get__cedula(self):
        return self.__cedula
    def set__cedula(self,cedula):
        self.__cedula=cedula        
        
    #* GET - SET __telefono    
    def get__telefono(self):
        return self.__telefono
    def set__telefono(self,telefono):
        self.__telefono=telefono
        
    #* METODO __str__
    def __str__(self):
            return (
                    '\nNombre       :'+self.__nombreCompleto+
                    '\n'+'Cedula       :'+self.__cedula+
                    '\n'+'Telefono     :'+str(self.__telefono)
                    )
 
'''
Clase de empleado por tiempo definido (EmpleadoDefinido)
Esta clase hereda de la clase empleado. Los nuevos atributos son:
• Número de plaza
• Salario base
• Duración de contrato en meses
Además, cuenta con un método que calcula el salario total. El empleado recibe un aumento del 2% sobre su salario base. 
'''       
 
class EmpleadoDefinido(Empleado):
    
    def __init__(self, nombreCompleto, cedula, telefono, nPlaza, salarioBase, duracion_contrato):
        super().__init__(nombreCompleto, cedula, telefono)   
        
        # Nuevos atributos
        self.__nPlaza=nPlaza
        self.__salarioBase=salarioBase
        self.__duracion_contrato=duracion_contrato
        
    #* GET - SET __nPlaza 
    def get__nPlaza(self):
        return self.__nPlaza
    def set__nPlaza(self,nPlaza):
        self.__nPlaza=nPlaza
        
    #* GET - SET __salarioBase
    def get__salarioBase(self):
        return self.__salarioBase
    def set__salarioBase(self,salarioBase):
        self.__salarioBase=salarioBase      
             
    #* GET - SET __duracion_contrato
    def get__duracion_contrato(self):
        return self.__duracion_contrato
    def set__duracion_contrato(self,duracion_contrato):
        self.__duracion_contrato=duracion_contrato   
        
    def salario_total(self):
        return self.__salarioBase+(self.__salarioBase*2/100)       
    
'''
Clase de empleado por tiempo indefinido
Esta clase hereda de la clase empleado. Los nuevos atributos son:
• Número de plaza
• Salario base
• Categoría (1, 2, 3)
Además, cuenta con un método que calcula el salario total Los empleados reciben un aumento de acuerdo a su categoría:
• Categoría 1: 3%
• Categoría 2: 5%
• Categoría 3: 8%
'''    

class EmpleadoIndefinido(Empleado):
    def __init__(self, nombreCompleto, cedula, telefono, nPlaza, salarioBase, categoria):
        super().__init__(nombreCompleto, cedula, telefono)
        
        #Atributos nuevos para la clase
        self.__nPlaza=nPlaza
        self.__salarioBase=salarioBase
        self.__categoria=categoria
        
     #* GET - SET __nPlaza 
    def get__nPlaza(self):
        return self.__nPlaza
    def set__nPlaza(self,nPlaza):
        self.__nPlaza=nPlaza
        
    #* GET - SET __salarioBase
    def get__salarioBase(self):
        return self.__salarioBase
    def set__salarioBase(self,salarioBase):
        self.__salarioBase=salarioBase    
        
    #* GET - SET __categoria
    def get__categoria(self):
        return self.__categoria
    def set__categoria(self,categoria):
        self.__categoria=categoria    
    
    #Segun la categoria 1, 2 ó 3 el incremento es 3%,5%,8% y sino 0%, y devuelve el __salarioBase            
    def salario_total(self):
        if self.__categoria==1:
            incremento=3
        elif self.__categoria==2:
            incremento=5
        elif self.__categoria==3:
            incremento=8    
        else:
            incremento=0
        return self.__salarioBase + (self.__salarioBase*incremento/100) 
    
    def __str__(self):
        return ('\n'+(self.__class__.__name__)+ 
                super().__str__()+
                "\nNum.Plaza    : "+
                str(self.get__nPlaza()) +
                "\nSalario Base :"+str(self.get__salarioBase())+
                "\nCategoria    :"+str(self.get__categoria()))  
        
'''
Empleado subcontratado
Esta clase hereda de la clase empleado. 
El nuevo atributo es:
• Empresa responsable

'''     
class EmpleadoSubcontratado(Empleado):
    
    def __init__(self, nombreCompleto:str, cedula:str, telefono:int,empreResponsable:bool):
        super().__init__(nombreCompleto, cedula, telefono)
        self.__empresaResponsable=empreResponsable
    
    #* GET - SET __empresaResponsable
    def get__empresaResponsable(self):
        if self.__empresaResponsable:
            return "SI"
        else:
            return "NO"
        
    def set__empresaResponsable(self,empresaResponsable):
        self.__empresaResponsable=empresaResponsable 
        
    def __str__(self):
        return ('\n'+(self.__class__.__name__)+
                      super().__str__()+
                '\n'+'Responsable  :'+str(self.get__empresaResponsable())
                )    
    
   
#* ------------ PROGRAMA PRINCIPAL ----------------------------------------------------------------------------

empleado1=Empleado("Felix Lopez","67823456",653537550)
empleado1.set__telefono(643537958)
print(empleado1)       

empleadoDef1=EmpleadoDefinido("Pepe","1234567",643537956,100,1000,3)

print(empleadoDef1) 
print("\nSalario Base Empledo Def1               :", empleadoDef1.get__salarioBase())
print("Salario con aumento 2% de Empleado Def1 :", empleadoDef1.salario_total())

empleadoIndef1=EmpleadoIndefinido("Javier","7078504",6059741,300,2000,3)
print("Empleado Indefinido 1:")
print(empleadoIndef1)
print("\nEl salario de empleadoIndef1, con aumento es: ", empleadoIndef1.salario_total())
#! Para asignar una categoria hay que pasar el valor como parametro y NO IGUALAR, empleadoIndef1.set__categoria()=4
empleadoIndef1.set__categoria(4)    # coloco una categoria 4, que no existe asi que el aumento seria 0%

print(empleadoIndef1)
print("\nEl salario de empleadoIndef1, con aumento es: ", empleadoIndef1.salario_total())

empleadoSubC1=EmpleadoSubcontratado("Pepito Perez", "7865498G",9116578,True)
print(empleadoSubC1)

#EJEMPLO COLOCADO EN EL TEXTO DEL CURSO ( LO ADAPTE A LOS CAMBIOS DE NOMBRE QUE HICE)

#Empleados subcontratados
subContratado1 = EmpleadoSubcontratado("Roberto Flores Morales", 123456789, 88888888,"Coca-Cola")
subContratado2 = EmpleadoSubcontratado("Ana Mora Cruz", 223446789, 77777777, "Pepsi")
print("\n*** Empleados subcontratados ***")
print("\n****Empleado 1****")
print("Nombre             : " + subContratado1.get__nombreCompleto() +
    "\nCédula             : " + str(subContratado1.get__cedula()) +
    "\nTeléfono           : " + str(subContratado1.get__telefono()) +
    "\nEmpresa responsable: " + subContratado1.get__empresaResponsable())
print("\n****Empleado 2****")
print("Nombre             : " + subContratado2.get__nombreCompleto() +
    "\nCédula             : " + str(subContratado2.get__cedula()) +
    "\nTeléfono           : " + str(subContratado2.get__cedula()) +
    "\nEmpresa responsable: " + subContratado2.get__empresaResponsable())

#Empleados por tiempo definido
empleadoD = EmpleadoDefinido("Jeff Muñoz Castro", 345687324, 66666666, 3, 500000, 3)
empleadoD2 = EmpleadoDefinido("María Gonzáles Pérez", 983456783, 99999999, 6, 450000, 2)

print("\n*** Empleados de tiempo definido ***")
print("\n****Empleado 1****")
print("Nombre           : " + empleadoD.get__nombreCompleto() +
    "\nCédula           : " + str(empleadoD.get__cedula()) +
    "\nTeléfono         : " + str(empleadoD.get__telefono()) +
    "\nNúmero de plaza  : " + str(empleadoD.get__nPlaza()) +
    "\nDuracion contrato: " + str(empleadoD.get__duracion_contrato()) + " meses" +
    "\nSalario total    : " + str(empleadoD.salario_total()))
print("\n****Empleado 2****")
print("Nombre           : " + empleadoD2.get__nombreCompleto() +
    "\nCédula           : " + str(empleadoD2.get__cedula()) +
    "\nTeléfono         : " + str(empleadoD2.get__telefono()) +
    "\nNúmero de plaza  : " + str(empleadoD2.get__nPlaza()) +
    "\nDuración contrato: " + str(empleadoD2.get__duracion_contrato()) + " meses" +
    "\nSalario total    : " + str(empleadoD2.salario_total()))

empleadoI = EmpleadoIndefinido("Roberto Rojas Salazar", 434565432, 22222222, 4, 350000,
1)
empleadoI2 = EmpleadoIndefinido("Rebeca Suárez Tapia", 897456274, 33445533, 7, 510000, 2)
empleadoI3 = EmpleadoIndefinido("Sara Vega Montes", 989734567, 65786590, 19, 475000, 3)
empleadoI4 = EmpleadoIndefinido("Luis Sánchez Castillo", 546378763, 23546543, 23, 560000,
1)
print("\n*** Empleados de tiempo indefinido ***")
print("\n****Empleado 1****")
print("Nombre           : " + empleadoI.get__nombreCompleto() +
    "\nCédula           : " + str(empleadoI.get__cedula()) +
    "\nTeléfono         : " + str(empleadoI.get__telefono()) +
    "\nNúmero de plaza  : " + str(empleadoI.get__nPlaza()) +
    "\nCategoría        : " + str(empleadoI.get__categoria()) +
    "\nSalario total    : " + str(empleadoI.salario_total()))
print("\n****Empleado 2****")
print("Nombre           : " + empleadoI2.get__nombreCompleto() +
    "\nCédula           : " + str(empleadoI2.get__cedula()) +
    "\nTeléfono         : " + str(empleadoI2.get__telefono()) +
    "\nNúmero de plaza  : " + str(empleadoI2.get__nPlaza()) +
    "\nCategoría        : " + str(empleadoI2.get__categoria()) +
    "\nSalario total    : " + str(empleadoI2.salario_total()))
print("\n****Empleado 3****")
print("Nombre           : " + empleadoI3.get__nombreCompleto() +
    "\nCédula           : " + str(empleadoI3.get__cedula()) +
    "\nTeléfono         : " + str(empleadoI3.get__telefono()) +
    "\nNúmero de plaza  : " + str(empleadoI3.get__nPlaza()) +
    "\nCategoría        : " + str(empleadoI3.get__categoria()) +
    "\nSalario total    : " + str(empleadoI3.salario_total()))
print("\n****Empleado 4****")
print("Nombre           : " + empleadoI4.get__nombreCompleto() +
    "\nCédula           : " + str(empleadoI4.get__cedula()) +
    "\nTeléfono         : " + str(empleadoI4.get__telefono()) +
    "\nNúmero de plaza  : " + str(empleadoI4.get__nPlaza()) +
    "\nCategoría        : " + str(empleadoI4.get__categoria()) +
    "\nSalario total    : " + str(empleadoI4.salario_total()))

        
        