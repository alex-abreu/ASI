class Text:

	#adds value at the end of the string
	def add_value(self, list_in, value_string):
		list_out = set()
		for item in list_in:
			list_out.add(item+value_string)
		return list_in.union(list_out)
		

	
	#returns a list with all itens alternating betwen lower and upper case starts with upper case
	def alternate(self, list_in, start):
		list_out = set()
		
		if start == "upper":
			for item in list_in:
				res = [ele.upper() if not idx % 2 else ele.lower() for idx, ele in enumerate(item)] 
				res = "".join(res)
				list_out.add(res)
				res=""
		elif start == "lower":
			for item in list_in:
				res = [ele.lower() if not idx % 2 else ele.upper() for idx, ele in enumerate(item)] 
				res = "".join(res)
				list_out.add(res)
				res=""
		return list_in.union(list_out)
	
	#returns a list with everything on lower case OR uppercase
	def LUCase(self, list_in, case):
		list_out = set()
		
		if case == "upper":
			for item in list_in:
				list_out.add(item.upper())
		elif case == "lower":
			for item in list_in:
				list_out.add(item.lower())
		return list_in.union(list_out)

	#replace all 'a's and 'A's with '@'
	def replaceA(self, list_in):

		list_out = set()
		
		for item in list_in:
			list_out.add(item.replace('a','@').replace('A','@'))

		return list_in.union(list_out)  
	
	#replace all 'e's 'E's with '3'
	def replaceE(self, list_in):

		list_out = set()
		
		for item in list_in:
			list_out.add(item.replace('e','3').replace('E','3'))

		return list_in.union(list_out)

	#replace all 'i's 'I's with '1' OR '!'
	def replaceI(self, list_in, type):

		list_out = set()
		
		if type == 1:
			for item in list_in:
				list_out.add(item.replace('i','1').replace('I','1'))
		elif type == "!":
			for item in list_in:
				list_out.add(item.replace('i','!').replace('I','!'))
		return list_in.union(list_out)

	#replace all 'o's 'O's with '0'
	def replaceO(self, list_in):

		list_out = set()
		
		for item in list_in:
			list_out.add(item.replace('o','0').replace('O','0'))

		return list_in.union(list_out)

	#generates a list of passwords
	def generate(self, list_in):
		list_in = self.add_value(list_in, "123")
		list_in = self.add_value(list_in, "456")
		list_in = self.add_value(list_in, "321")
		list_in = self.replaceA(list_in)
		list_in = self.replaceE(list_in) 
		list_in = self.replaceI(list_in, 1) 
		list_in = self.replaceI(list_in, "!")
		list_in = self.replaceO(list_in)
		list_in = self.alternate(list_in, "upper")
		list_in = self.alternate(list_in, "lower")
		list_in = self.LUCase(list_in, "upper")
		list_in = self.LUCase(list_in, "lower")
		print(len(list_in))
		return list_in


