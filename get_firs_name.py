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
	
	in_names = readFile("simpsons_personagens.txt")

	list_out = []
	for names in in_names:

		lName = names.split()
		list_out.append(lName[0])
	WriteFile('simpsons_personagens_fName.txt',list_out)