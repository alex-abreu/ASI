def readFile(fName):
	list_out = []
	file = open(fName,"r")
	for line in file:
		if "\n" in line:
			list_out.append(line[:-1])
		else:
			list_out.append(line)

	return list_out

def get_dic_hashList(f1,f2):
	
	resultDic = {}

	f1_in = readFile(f1)
	f2_in = readFile(f2)

	for origin,hashK in zip(f1_in,f2_in):
		resultDic[origin] = hashK

	return resultDic, f2_in

def compare(dic , hash_list):

	list_out = []

	for index in dic:
		if dic[index] in hash_list:
			list_out.append(index)

	return list_out
