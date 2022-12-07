import time
number1 = None
number2 = None
number3 = None
number4 = None

Luz_Verde = [0, 1, 1, 1]
Luz_Amarilla = [1, 0, 1, 1]
Luz_Roja = [1, 1, 0, 1]
Luz_Cruce = [1, 1, 1, 0]

def waiting():
        print("Por 5seg")
        time.sleep(1)
        print("5")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)

        return None


def ELuz_Verde(num1, num2, num3, num4):
    
    if num1 == Luz_Verde[0] and num2 == Luz_Verde[1] and num3 == Luz_Verde[2] and num4 == Luz_Verde[3]:
        print("Verde Encendido")
        waiting()
    else:
        time.sleep(0.2)
        return print("No Encendido")

def ELuz_Amarilla(num1, num2, num3, num4):
    if num1 == Luz_Amarilla[0] and num2 == Luz_Amarilla[1] and num3 == Luz_Amarilla[2] and num4 == Luz_Amarilla[3]:
        print("Amarillo Encendido")
        waiting()
    else:
        time.sleep(0.2)
        return print("No Encendido")

def ELuz_Roja(num1, num2, num3, num4):
    if num1 == Luz_Roja[0] and num2 == Luz_Roja[1] and num3 == Luz_Roja[2] and num4 == Luz_Roja[3]:
        print("Rojo Encendido")
        waiting()
    else:
        time.sleep(0.2)
        return print("No Encendido")


def ELuz_Cruce(num1, num2, num3, num4):
    if num1 == Luz_Cruce[0] and num2 == Luz_Cruce[1] and num3 == Luz_Cruce[2] and num4 == Luz_Cruce[3]:
        print("Cruce Encendido")
        waiting()
    else:
        time.sleep(0.2)
        return print("No Encendido")




while True:
    print("Introduzca los estados (1/0) de las compuertas, son 4 de estas")
    
    number1 = int(input("Introduzca el 1er numero: "))
    number2 = int(input("Introduzca el 2do numero: "))
    number3 = int(input("Introduzca el 3er numero: "))
    number4 = int(input("Introduzca el 4to numero: "))
    
    print("----Chekando Luz Verde----")
    ELuz_Verde(number1, number2, number3, number4)
    time.sleep(1)
    print("----Chekando Luz amarilla----")
    ELuz_Amarilla(number1, number2, number3, number4)
    time.sleep(1)
    print("----Chekando Luz Roja----")
    ELuz_Roja(number1, number2, number3, number4)
    time.sleep(1)
    print("----Chekando Luz Cruce----")
    ELuz_Cruce(number1, number2, number3, number4)
    time.sleep(1)