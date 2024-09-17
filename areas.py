from funciones import *

while (True):
    menu()
    op=int(input("digite una opcion:"))
    if (op==1):
        l=int(input("digite un lado del cuadrado "))
        print(f"el area del cuadrado es: {areacuadrado(l)}")
    elif(op==2):
        b=int(input("digite la base del traingulo "))
        h=int(input("digite la altura "))
        print(f"el area del tringulo es: {areatriangulo(b,h)}")
    elif(op==3):
        b=int(input("digite la base del retangulo "))
        h=int(input("digite la altura "))
        print(f"el area del retangulo es: {arearetangulo(b,h)}")
    elif(op==4):
        p=int(input("digite la base del pentagono "))
        a=int(input("digite la altura "))
        print(f"el area del pentagono es: {areapentagono(p,a/2)}")
    elif(op==5):
        break