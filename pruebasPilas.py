from Pila import Stack

pila=Stack()

pila.push('a')
pila.push('x')
pila.to_string()
pila.push('b')
pila.push('y')
pila.to_string()
var=pila.pop()
pila.to_string()
print(f"var={var}")
