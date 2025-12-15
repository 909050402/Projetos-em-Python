import os
from tkinter.filedialog import askdirectory

#aqui eu vou perguntar pro usuário onde ele vai querer salvar as pastas que iremos criar abaixo
caminho = askdirectory(title="escolha onde serão salvos os arquivos abaixo")

#aqui é um exemplo das pastas que irei criar, podem ser o nome dos funcionários de uma empresa, e eu poderia usar o pandas pra pegar essas informações de uma base de dados
lista = ["mateus","roberto","joão","pedro","jorge","maria","alice"]

for nomes in lista:
    os.mkdir(os.path.join(caminho,nomes))