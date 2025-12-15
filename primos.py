

a = int(input("digite um numero: "))
numeros = []
ncousin = []
divisores = []

#aqui estou fazendo o seguinte primeiro eu começo colocando o numero pra saber se ele é primo ou não
# depois eu faço o numero primo mod 1 até chegar ao antecessor dele
# se o numero é primo eu quero saber os divisores do número
for i in range(1,a - 1):
    conta = a%(a-i)
    numeros.append(conta)
    if conta == 0:
        divisores.append(a-i)
if 0 in numeros:
    ncousin.append(a)
    print("numero não primo")
    print(divisores)
    x = len(divisores)
    print(f"o número {a} possui {x} números que são divisões exatas")
else:
    print("numero primo")
        
    
