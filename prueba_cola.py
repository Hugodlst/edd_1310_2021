from colas import Queue, BoundePriorityQueue

q1=Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())

print("Prueba 2 de Queue")
c1={"id":1, "nombre":"Mario", "balance":20.5}
c2={"id":2, "nombre":"Diana", "balance":3456.5}
c3={"id":3, "nombre":"Bartolo", "balance":1000000.0}

atencion=Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
siguiente=atencion.dequeue()
print(f"Bienvenidoar. {siguiente['nombre']}, en que podemos servirle el dia de hoy")
print(atencion.to_string())

print("Pruebas de la colas con prioridad acotada")

maestres={"prioridad":4,"descripcion":"Maestres","personas":["Juan  P","Diego H"]}
niños={"prioridad":2,"descripcion":"Niños","personas":["Pepe J","Carolina F"]}
mecanicos={"prioridad":4,"descripcion":"Mecanicos","personas":["Rodrigo G","Santiango N"]}

cpa=BoundePriorityQueue(7)
cpa.enqueue(maestres['prioridad'], maestres)
cpa.enqueue(maestres['prioridad'], maestres)
cpa.enqueue(maestres['prioridad'], maestres)
