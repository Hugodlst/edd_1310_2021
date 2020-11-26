class Stack:
    def __init__(self):
        self.__data=list()

    def is_empty(self):
        return len(self.__data)==0 #Se pregunta de cuanta es la longitud

    def length(self):
        return len(self.__data) #Ve los elementos de la lista en cuestion de longitud

    def pop(self):
        if self.is_empty():
            print("pila vacía")
        else:
            return self.__data.pop() #Elimina el ultimo elemento de la lista

    def push(self,value):
        self.__data.append(value)

    def peek(self):
        return self.__data[ len(self.__data)-1]

    def to_string(self):
        print(" -----")
        for item in self.__data:
            print(f" | {item} |")
            print(" -----")
