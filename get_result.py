
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
	f = open(fName, "a")
	for item in list_in:
		f.write(item)
		f.write('\n')
	f.close()

if __name__ == '__main__':
	
	fList = readFile('out.txt')
	
	output = 'simpsons_dic.txt'
	
	for file in fList:
		temp_list = readFile(file)
		WriteFile(output, temp_list)


