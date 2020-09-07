class Text:

	def replaceA(self, list_in):

		list_out = []
		
		for item in list_in:
			list_out.append(item.replace('a','@'))

		return list_out  
	
	def replaceE(self, list_in):

		list_out = []
		
		for item in list_in:
			list_out.append(item.replace('e','3'))

		return list_out

	def replaceI(self, list_in):

		list_out = []
		
		for item in list_in:
			list_out.append(item.replace('i','1'))

		return list_out

	def replaceO(self, list_in):

		list_out = []
		
		for item in list_in:
			list_out.append(item.replace('o','O'))

		return list_out

	def replaceALL(self, list_in):

		list_out = []
		
		for item in list_in:
			wordA = item.replace('a','@').replace('e','3').replace('i','1').replace('o','0')
			list_out.append(wordA)

		return list_out

if __name__ == '__main__':
	
	list_in = ['bAnAnA', 'abacate', 'abacaxi']
	t =Text()
	print(t.replaceALL(list_in))