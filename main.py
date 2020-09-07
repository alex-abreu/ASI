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
	
	fList = ['alt_Simpsons_reg','alt_Simpsons_reg_123', 'alt_Simpsons_reg_147', 'alt_Simpsons_reg_159',
			'alt_Simpsons_rep','alt_Simpsons_rep_123','alt_Simpsons_rep_147','alt_Simpsons_rep_159',
			'reg_simpsons_alt','reg_simpsons_alt_123','reg_simpsons_alt_147','reg_simpsons_alt_159',
			'reg_simpsons_alt']

	for fName in fList:
		names = readFile(fName+'.txt')
		WriteFile("no_space"+fName+'.txt',strip_space(names))