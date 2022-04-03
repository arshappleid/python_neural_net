import random
class buy:
	def __init__(self, closeData):
		## class attributes
		self.closeData = closeData

	def should_buy(self):
		## will return boolean, if we should buy the stock or not.
		ans = self.method_1() + self.method_2() + self.method_3() + self.method_4() + self.method_5()
		if(ans>=3):
			return True;
		return False;


	def method_1(self):
		return random.randint(0,1)
	
	def method_2(self):
		return random.randint(0,1)

	def method_3(self):
		return random.randint(0,1)
	
	def method_4(self):
		return random.randint(0,1)

	def method_5(self):
		return random.randint(0,1)

	
