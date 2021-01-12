def factorial(n):
    if n==0:
        return 1
    else:
        return factorial(n-1)*n

def fibonacci(n):
    if n==1 or n==0:
        return n
    if n>1:
        return(fibonacci(n-1) + fibonacci(n-2))

def main():
    for num in range(1,11,1):
        r=factorial(num)
        print(f"El factorial de {num} es {r} ")

def printRev(n): #Recibe un valor 3
    if n>0:
        #print(n)
        printRev(n-1)
        print(n)


def main2():
    printRev(3)

def main3():
    for num in range (11):
        print(str(fibonacci(num))+",",end="")
    print("")

main3()
