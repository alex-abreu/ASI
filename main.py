from generate import *

import glob

#Obtém a primeira e última palavras de uma string(separação por espaços)
def getFirstAndLast(name):
	namesList = name.split(" ")
	return namesList[0], namesList[-1]

#Cria nomes separados para senhas que contém parênteses
def getParentheses(list_in):
	list_out = set()
	for item in list_in:
		if "(" not in item and ")" not in item:
			continue
		namesList = item.split("(")
		list_out.add(item.replace(")", "").replace("(", ""))
		for j in range(0, len(namesList)):
			list_out.add(namesList[j])
	return list_in.union(list_out)

#remove apóstrofos de strings e as insere na lista	
def removeApostrophe(list_in):
	list_out = set()
	for item in list_in:
		if "'" in item:
			list_out.add(item.replace("'", ""))
	return list_in.union(list_out)
	
#gera o arquivo com o dicionário
def WriteFile(fName, list_in):
	f = open(fName, "w")
	for item in list_in:
		f.write(item)
		f.write('\n')
	f.close()

# "substitui" espaços por underlines(adicionando novos itens). 
# Não remove os itens originais com espaços.
def underline_space(list_in):
	list_out = set()

	for item in list_in:
		list_out.add(item.replace(" ", "_"))
	return list_in.union(list_out)

#Remove espaços das strings da lista.
def strip_space(list_in):
	list_out = []
	for item in list_in:
		list_out.append(item.replace(" ", ""))
	return set(list_out)

if __name__ == '__main__':

	origin = []
	for file in glob.glob('dicionários\\*.txt'):
		origin += open(file, 'r').read().split('\n')
	origin = list(set(origin))
	size = len(origin)
	#pega o nome e sobrenome(cada um vira uma string separada) e adiciona-os na lista
	#sem remover a string original
	for i in range(0, size):
		origin[i] = origin[i].strip()
		first, last = getFirstAndLast(origin[i])
		origin.append(first)
		origin.append(last)
	origin = set(origin)
	t = Text()
	
	origin = removeApostrophe(origin)
	origin = underline_space(origin)
	origin = strip_space(origin)
	origin = getParentheses(origin)
	origin = t.generate(origin)
	origin.discard('')
	origin.discard(" ")
	
	WriteFile("dicionários\\alterados\\final.txt", origin)

	