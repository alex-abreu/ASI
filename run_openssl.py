
import os
import sys
import io
import glob

path = 'dicionários\\'
#lista de senhas
nameList = []
#obtendo os dicionários e formando a lista de senhas
for file in glob.glob(path+'*.txt'):
    nameList += open(file, 'r').read().split('\n')

#lista de nomes dos arquivos criptografados
fileList = [f"file{i}.enc" for i in range(1,31)]

# para cada arquivo criptografado
for i in range(0, 30):
   #para cada senha em nameList
   for j in range(0, len(nameList)):
       #comando cmd pra decifrar
       print(f'tentativa {j} de {len(nameList)} do arquivo {i+1}')
       error = os.system(f'cmd /c "openssl enc -d -aes-256-cbc -pbkdf2 -salt -in {fileList[i]} -out decifrado{i+1}.txt -pass pass:"{nameList[j]}"')
       #se retorno == 0 não houve erro ao decifrar o arquivo
       if error == 0:
           print(f"Opa! Conseguimos decifrar um arquivo! O arquivo é {fileList[i]}, e a senha é: {nameList[j]}\n")
           break




