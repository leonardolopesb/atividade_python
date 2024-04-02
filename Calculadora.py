import math

class Calculadora:

    @staticmethod
    def Operacoes(x, y, tipo):
        match tipo:
            case 1:
                return x + y
            
            case 2:
                return x - y
            
            case 3:
                return x * y
            
            case 4:
                return x / y
            
            case 5:
                return math.pow(x,y)
            
            case 6:
                return math.sqrt(x)

print("Digite o primeiro valor: ")
a = input()
a = float(a)

print("Digite o segundo valor: ")
b = input()
b = float(b)

print("\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Expoência\n6 - Raiz quadrada\n")

print("Escolha o tipo de operação para realizar:")

tipo = input()
tipo = int(tipo)

print(Calculadora.Operacoes(a, b, tipo))
