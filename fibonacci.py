#sequencia fibonacci se inicia por 0 e 1 e o proximo valro sera a soma dos 
#numeros anteriores

entrada = input("Informe um número inteiro:\n")
entrada_int = int(entrada)
f1 = 0
f2 = 1
f3 = 0
n = 0

while entrada_int > f3:
    f3 = f1 + f2
    f1 = f2
    f2 = f3        
    if n == 100:
        break
        n += 1
if entrada_int == 0 or entrada_int == 1:
    print("O número informado faz parte da Sequência de Fibonacci.")
elif entrada_int == f3:
    print("O número informado faz parte da Sequência de Fibonacci.")
else:
    print("O número informado não faz parte da Sequência de Fibonacci.")   

