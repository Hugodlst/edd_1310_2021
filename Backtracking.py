from Array2D import Array2D
from Stack import Stack

class LaberintoADT:

    #0 pasillo, 1 pared, S de salida y E de entrada
    #pasillo es una tupla( (2,1), (2,2), (2,3), (2,4), (3,2), (4,2) )
    #entrada en una tupla(5,1)
    #salida(2,5)

    def __init__( self, rens, cols, pasillos, entrada, salida):
        self.__laberinto=Array2D( rens, cols, '1')
        for pasillo in pasillos:
            self.__laberinto.set_item( pasillo[0], pasillo[1], '0')
        self.set_entrada(entrada[0],entrada[1])
        self.set_salida(salida[0],salida[1])
        self.__camino=Stack()
        self.__previa=None


    def to_string(self):
        self.__laberinto.to_string()

#Establece la entrada 'E' en la matriz, vrereficar limites

    def set_entrada(self, ren, col):
        #Terminar la validacion de las coordenadas
        self.__laberinto.set_item( ren, col, 'E')

#Establecer salida, denro de los limites perifericos de la matriz

    def set_salida(self, ren, col):
        #Terminar las validaciones
        self.__laberinto.set_item( ren, col, 'S')

    def es_salida(self, ren, col):
        return self.laberinto.get_item(ren, col)=='S'

    def buscar_entrada(self):
        econtrado=False
        for renglon in range(self.__laberinto.get_num_rows()):
            for columna in range(self.__laberinto.get_num_cols()):
                if self.__laberinto.get_item(renglon, columna)=='E':
                    self:__camino.push(tuple(renglon,columna))
                    econtrado=True
        return encontrado

    def set_previa(self, pos_previa):
        self.__previa=pos_previa

    def get_previa(self):
        return self.__previa

    def resolver_laberinto(self):
        #Aplicar Regla
