def suma(a,b):
    return a +b
def resta(a,b):
    return a -b
def division(a,b):
    if b==0:
        return "Error: División por cero no permitida"
    return a/b
def multiplicacion(a,b):
    return a*b

def mostrar_menu():
    print("\nPor favor presiona una opcion para la calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opcción (1,2,3,4,5)")


    if opcion==5:
        break

    num1=float(input("\nSeleccionar el primer numero:"))
    num2=float(input("\nSeleccionar el segundo numero:"))

    if opcion=="1":
        print(f"El resultado es {suma(num1,num2)}")
    if opcion=="2":
        print(f"El resultado es {resta(num1,num2)}")
    if opcion=="3":
        print(f"El resultado es {multiplicacion(num1,num2)}")
    if opcion=="4":
        print(f"El resultado es {division(num1,num2)}")

        
