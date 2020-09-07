class Text:

	#returns a list with all itens alternating betwen lower and upper case starts with upper case
	def alternate(self, list_in):
		
		list_out = []

		for list_item in list_in:
			res = [ele.upper() if not idx % 2 else ele.lower() for idx, ele in enumerate(list_item)] 
			res = "".join(res)
			list_out.append(res)
			res=""

		return list_out
	
	#same as alternate but starts with lower
	def alternateL(self, list_in):
		
		list_out = []

		for list_item in list_in:
			res = [ele.lower() if not idx % 2 else ele.upper() for idx, ele in enumerate(list_item)] 
			res = "".join(res)
			list_out.append(res)
			res=""

		return list_out
	

	#returns a list with everything on lower case
	def LowerCase(self, list_in):
		
		list_out = []

		for item in list_in:
			list_out.append(item.lower())

		return list_out

	#replace all 'a's 'A's with '@'
	def replaceA(self, list_in):

		list_out = []
		
		for item in list_in:
			list_out.append(item.replace('a','@').replace('A','@'))

		return list_out  
	
	#replace all 'e's 'E's with '3'
	def replaceE(self, list_in):

		list_out = []
		
		for item in list_in:
			list_out.append(item.replace('e','3').replace('E','3'))

		return list_out

	#replace all 'i's 'I's with '1'
	def replaceI(self, list_in):

		list_out = []
		
		for item in list_in:
			list_out.append(item.replace('i','1').replace('I','1'))

		return list_out

	#replace all 'o's 'O's with '0'
	def replaceO(self, list_in):

		list_out = []
		
		for item in list_in:
			list_out.append(item.replace('o','0').replace('O','0'))

		return list_out

	#replace all 'a' 'e' 'i' 'o' with they numeric counterpart, same for upper case
	def replaceALL(self, list_in):

		list_out = []
		
		for item in list_in:
			list_out.append(item.replace('a','@').replace('e','3').replace('i','1').replace('o','0')
				.replace('O','0').replace('I','1').replace('E','3').replace('A','@'))

		return list_out

class Merge:

	def merge2(self, lis1,lis2):
		
		list_out = []
		
		for item1 in lis1:
			for item2 in lis2:
				list_out.append(item1+item2)

		return list_out

	def merge3(self, lis1,lis2,lis3):
		
		list_out = []
		
		for item1 in lis1:
			for item2 in lis2:
				for item3 in lis3:
					list_out.append(item1+item2+item3)

		return list_out
