from arbolesbinarios import BinarySearchTree

abb=BinarySearchTree()
abb.__insert(50)
abb.__insert(35)
abb.__insert(30)
abb.__insert(60)
abb.__insert(89)
abb.__insert(70)

abb.transversal()
abb.transversal("preorden")
abb.transversal("posorden")
res=abb.search(24)
print(f"El resultado es: { res }")
abb.remove(35)
abb.transversal()
