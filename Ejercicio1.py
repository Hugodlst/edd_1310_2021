def suma_lista_rec(lista):
    if len(lista)==1:
        return lista[0]
    else:
        return lista.pop()+suma_lista_rec(lista)

def main():
    datos=[4,2,3,5] #14
    res=suma_lista_rec
