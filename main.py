from generate import *

#reads the file fName file and creates a list
#with the names in the file
def readFile(fName):
	list_out = []
	file = open(fName,"r")
	for line in file:
		if "\n" in line:
			list_out.append(line[:-1])
		else:
			list_out.append(line)

	return list_out

def WriteFile(fName, list_in):
	f = open(fName, "w")
	for item in list_in:
		f.write(item)
		f.write('\n')
	f.close()

if __name__ == '__main__':
	
	t = Text()

	list_in = readFile('simpsons_personagens.txt')

	WriteFile("alt_Simpsons_reg.txt",t.alternate(list_in))
	WriteFile("alt_Simpsons_rep.txt",t.replaceALL(t.alternate(list_in)))
	WriteFile("reg_simpsons_alt.txt",t.replaceALL(list_in))
	
