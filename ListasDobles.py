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
        if self.__head.data==value:
            self.__head=self.__head.siguiente
        else:
            anterior=None #Para borrar el primero
            while curr_node.data != value and curr_node.siguiente !=None:
                anterior=curr_node
                curr_node=curr_node.siguiente
            if curr_node.data==value:
            #print("ACTUAL:",anterior.data)
                anterior.siguiente=curr_node.siguiente
            else:
                print("El dato no existe en la lista")

    def preppend(self,value):
        nuevo=Nodo(value,self.__head)
        self.__=nuevo

    def tail(self):
        curr_node=self.__head
        while curr_node.siguiente !=None:
            curr_node=curr_node.siguiente
        return curr_node

    def get(self,posicion=None): #Por defecto regresa el ultimo
        contador=0
        dato=None
        if posicion==None:
            dato=self.tail().data
        else:
            pass



        return dato

class NodoDoble:
    def __init__ (self,value,anterior=None,siguiente=None,):
        self.data=value
        self.next=siguiente
        self.prev=anterior

class DoubleLinkedList:
    def __init__(self):
        self.__head=NodoDoble(None)
        self.__tail=NodoDoble(None)
        self.__size=0

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size==0

    def append(self , value ):
        if self.is_empty() :
            nuevo = NodoDoble( value )
            self.__head = nuevo
            self.__tail = nuevo
        else:
            nuevo = NodoDoble(value , self.__tail , None )
            self.__tail.next = nuevo
            self.__tail = nuevo
        self.__size += 1

    def transversal( self ):
        curr_node = self.__head
        while curr_node != None:
            print(f"<-- { curr_node.data } --> " , end="")
            curr_node = curr_node.next
        print("")

    def reverse_transversal( self ):
            curr_node = self.__tail
            while curr_node != None:
                print(f"<-- { curr_node.data } --> " , end="")
                curr_node = curr_node.prev
            print("")

    def remove_from_head(self,value):
        curr_node=self.__head
        while curr_node.data != value and curr_node != None: #!= es diferente
               curr_node=curr_node.next
        if curr_node.data == value:
            self.__head = self.__head.next
            self.__head.prev = None

        curr_node.next =None
        curr_node.prev =None
        self.__size -= 1






#Punto Importante
#curr.prev(es todo el nodo anterior de un nodo de en medio).netx(agarra la cola de primer nodo para hacerlo igual al ultimo nodo)=curr.next
