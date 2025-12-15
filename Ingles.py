import pandas as pd
import random
import os
import subprocess

pergunta = []

resp = []

numeros = []

opçoes = []

df = pd.read_excel("Teste.xlsx")
#aqui eu leio a base de dados

ult = df["Palavra"].count() - 1

a = random.randint(0,ult)

resposta = df.iloc[a,1]

palavra = df.iloc[a,0]

resp.append(resposta)

pergunta.append(palavra)



for i in range(ult + 1):
    numeros.append(i)

numeros.pop(a)


aleatorios = random.sample(numeros,k=3)

for cada in aleatorios:
    valor = df.iloc[cada,1]
    opçoes.append(valor)
opçoes.extend(resp)

random.shuffle(opçoes)



caminho = r"C:\Users\admin\Projetos\Ingles"

path = r"C:\Users\admin\Projetos\Ingles\\"

n = int(a + 1)

arq = os.listdir(caminho)

arquivo = os.path.join(caminho, f"{n}.jpg")
if not os.path.exists(arquivo):
    arquivo = os.path.join(caminho, f"{n}.png")

subprocess.Popen([arquivo], shell=True)

x = pergunta[0].upper()
print(x)

for cada in opçoes:
    print(cada)

numero = int(input("escreva um numero de 1 a 4: ")) - 1

answer = opçoes[numero]

if answer in resp:
    print("resposta certa")
else:
    print("resposta errada")