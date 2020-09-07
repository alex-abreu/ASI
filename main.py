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

def strip_space(list_in):
	
	list_out = []

	for item in list_in:
		list_out.append(item.replace(" ", ""))
	return list_out

if __name__ == '__main__':
	
	fName = "lugares_simpsons.txt"
	origin = readFile(fName)

	t = Text()
	list_out = []
	list_out = list_out + origin
	
	temp = strip_space(origin)

	list_out = list_out + temp
	
	list_out = list_out + t.replaceALL(temp)
	list_out = list_out + t.alternate(temp)
	list_out = list_out + t.add_value(temp, "123")
	list_out = list_out + t.add_value(temp, "147")
	list_out = list_out + t.add_value(temp, "159")

	list_out = list_out + t.replaceALL(t.alternate(temp))
	list_out = list_out + t.add_value(t.replaceALL(t.alternate(temp)),"123")
	list_out = list_out + t.add_value(t.replaceALL(t.alternate(temp)),"147")
	list_out = list_out + t.add_value(t.replaceALL(t.alternate(temp)),"159")

	WriteFile("simpson_lugares_dicionario.txt", list_out)