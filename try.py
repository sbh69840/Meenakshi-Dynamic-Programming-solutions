class menu:
	def __init__(self):
		self.menu_dict = {}
	def __add__(self,item):
		self.menu_dict[item[0]]=item[1]
		return self
	def print_menu(self):
		for key,values in self.menu_dict.items():
			print("[ ",key,", ",values," ]")
m = menu()
m = m+('idly',20)+('sambar',30)+('Vada',40)+('Tunne',100)+('Balls',69)+('Harshith',0)
m.print_menu()