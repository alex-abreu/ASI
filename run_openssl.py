import os
import sys
import io
import glob

path = 'dicionários\\'
nameList = []
for file in glob.glob(path+'*.txt'):
    nameList += open(file, 'r').read().split('\n')
print(len(nameList))
for i in range(0, len(nameList)):
   nameList[i] = nameList[i].strip()
nameList = list(set(nameList))

fileList = [f"file{i}.enc" for i in range(1,31)]

decrypted = [''] * 30

#para cada senha em nameList
for j in range(0, 30):
   # para cada arquivo criptografado
   for i in range(0, len(nameList)):
       print(str(i) + ' de ' + str(len(nameList)))
       #se o arquivo atual já foi decifrado
       if decrypted[j] != '':
           continue
       #comando cmd pra decifrar
       os.system(f'cmd /c openssl enc -d -aes-256-cbc -pbkdf2 -salt -in {fileList[j]} -out decifrado{j}.txt -pass pass:{nameList[i]}') 
       #nome do arquivo de saída(pode ser o arquivo decifrado ou não)
       decFile = f"decifrado{j+1}.txt"
       #abre o arquivo para leitura(caso exista). Caso esteja vazio, o arquivo original não foi               #decifrado. Caso contrário, ele foi decifrado.
       try:
           with open(decFile, 'r') as file:
               if file.read() != '':
                   decrypted[j] = nameList[i]
                   print(f"Opa! Conseguimos decifrar um arquivo! O arquivo é {fileList[j]}, e a senha é: {nameList[i]}\n")
       except(FileNotFoundError):
           continue




