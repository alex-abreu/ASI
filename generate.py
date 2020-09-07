class Text:

	def LowerCase(self, list_in):
		
		list_out = []

		for item in list_in:
			list_out.append(item.lower())

		return list_out

	def replaceA(self, list_in):

		list_out = []
		
		for item in list_in:
			list_out.append(item.replace('a','@').replace('A','@'))

		return list_out  
	
	def replaceE(self, list_in):

		list_out = []
		
		for item in list_in:
			list_out.append(item.replace('e','3').replace('E','3'))

		return list_out

	def replaceI(self, list_in):

		list_out = []
		
		for item in list_in:
			list_out.append(item.replace('i','1').replace('I','1'))

		return list_out

	def replaceO(self, list_in):

		list_out = []
		
		for item in list_in:
			list_out.append(item.replace('o','0').replace('O','0'))

		return list_out

	def replaceALL(self, list_in):

		list_out = []
		
		for item in list_in:
			list_out.append(item.replace('a','@').replace('e','3').replace('i','1').replace('o','0')
				.replace('O','0').replace('I','1').replace('E','3').replace('A','@'))

		return list_out


if __name__ == '__main__':
	
	list_in = ['bAnAnA', 'abacate', 'abacaxi']
	t =Text()
	print(t.replaceALL(list_in))