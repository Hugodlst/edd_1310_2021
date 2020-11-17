class Nodo:
    def __init__(self, value, siguiente=None):
        self.data=value  #falta encapsulamiento (se hace debido a que es necesario proteger los codigos de los nodos)
        self.siguiente=siguiente

class LinkedList:
    def __init__(self):
        self.__head=None #Se crea vacia

    def is_empty(self):
        return self.__head==None #Aqui viene la decision si tiene un valor head o no

    def append(self,value):
        nuevo=Nodo(value)
        if self.__head==None:
            self.__head=nuevo#self.is_empti
        else:
            curr_node=self.__head
            while curr_node.siguiente != None:
                curr_node=curr_node.siguiente
            curr_node.siguiente=nuevo

    def transversal(self):
        curr_node=self.__head
        while curr_node !=None:
            print(f"{curr_node.data}-->",end="")
            curr_node=curr_node.siguiente
        print("")

    def remove(self,value):
        curr_node=self.__head #se apunta a __head
        while curr_node.data != value and curr_node.siguiente !=None:
            curr_node=curr_node.siguiente
        if curr_node.data==value:
