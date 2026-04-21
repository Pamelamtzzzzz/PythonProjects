class Persona:
    def __init__(self,nombre,apellidos,id_fiscal):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__id_fiscal = id_fiscal

    def get_id_fiscal(self):
        return self.__id_fiscal
    
    def set_id_fiscal(self):
        self.__id_fiscal = nuevo_id

#metodo saludar
from abc import ABC, abstractmethod
class Persona(ABC):
    @abstractmethod
    def saludar(self):
        pass


class Cliente(Persona):

    contador_clientes = 0

    def __init__(self, nombre, apellidos, id_fiscal, id_cliente, email):
        super().__init__(nombre,apellidos,id_fiscal)
        self.id_cliente = id_cliente
        self.email = email
        Cliente.contador_clientes += 1

    def saludar(self):
        print("Hola, soy cliente")

    @staticmethod
    def clientes_creados():
        return Cliente.contador_clientes
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
    def __eq__(self,other):
        return self.get_id_fiscal() == other.get_id_fiscal()
    
    def __del__(self):
        print("Cliente eliminado")


