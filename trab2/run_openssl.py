import os
import sys
import io
import glob
""" 
    openssl genrsa -out bob.key 2048 & openssl rsa -in bob.key -pubout -out bob.pub & openssl genrsa -out root.key 4096 & openssl rsa -in root.key -pubout -out root.pub & openssl rsautl -sign -in bob.pub -inkey root.key -out sigbob & openssl rsautl -inkey root.pub -pubin -in sigbob -out decbob.pub & openssl rand -out sec.key 32 & openssl rsautl -encrypt -pubin -inkey bob.pub -in sec.key -out session.key & openssl enc -aes-256-ctr -pbkdf2 -e -in message.txt -out encrypted.enc -pass file:sec.key & openssl rsautl -decrypt -inkey bob.key -in session.key -out decalice.key & openssl enc -d -aes-256-ctr -pbkdf2 -in encrypted.enc -out decrypted.txt -pass file:decalice.key
   
   
    # SK/PK do bob
    openssl genrsa -out bob.key 2048
    openssl rsa -in bob.key -pubout -out bob.pub
 
    # SK/PK root(CA)
    openssl genrsa -out root.key 4096
    openssl rsa -in root.key -pubout -out root.pub
 
    # Assinando a PK do bob com a SK root
    openssl rsautl -sign -in bob.pub -inkey root.key -out sigbob
 
    # Verificando a assinatura utilizando a PK root
    openssl rsautl -inkey root.pub -pubin -in sigbob -out decbob.pub
 
    #chave de sessão
    openssl rand -out sec.key 32
    openssl rsautl -encrypt -pubin -inkey bob.pub -in sec.key -out session.key
    
    #Segredo
    openssl enc -aes-256-ctr -pbkdf2 -e -in message.txt -out encrypted.enc -pass file:sec.key        
    
    #Bob decifra
    openssl rsautl -decrypt -inkey bob.key -in session.key -out decalice.key
    openssl enc -d -aes-256-ctr -pbkdf2 -in encrypted.enc -out decrypted.txt -pass file:decalice.key
"""
def generateSK(skName):
    return os.system(f'cmd /c "openssl genrsa -out {skName} 2048"')

def generatePK(pkName, skName):
    return os.system(f'cmd /c "openssl rsa -in {skName} -pubout -out {pkName}"')

def generateCSR(csrName, skName):
    return os.system(f'cmd /c "openssl req -new -key {skName} -out {csrName}"')

##Chave Raíz

#Gerar chave privada 
generateSK("root.key")

#Gerar chave pública
generatePK("root.pub", "root.key")

##Chave do Usuário

#Gerar chave privada 
generateSK("bob.key")

#Gerar chave pública
generatePK("bob.pub", "bob.key") 

##Certificado




