from Listas import LinkedList

l=LinkedList()
print(f"L está vacía? { l.is_empty()}")
l.append(10)
l.append(5)
l.append(7)
l.append(20)
print(f"L está vacía? { l.is_empty()}")
l.transversal()
