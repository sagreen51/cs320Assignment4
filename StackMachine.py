class StackMachine:
	def __init__(self):
		self.list = []
	def push(self, x):
		self.list.append(int(x))
	def pop(self):
		return self.list.pop()
	def add(self):
		temp = StackMachine.pop(self) + StackMachine.pop(self)
		StackMachine.push(self,temp)
	def sub(self):
		temp = StackMachine.pop(self) - StackMachine.pop(self)
		StackMachine.push(self,temp)
	def mul(self):
		temp = StackMachine.pop(self) * StackMachine.pop(self)
		StackMachine.push(self,temp)
	def div(self):
		temp = StackMachine.pop(self) / StackMachine.pop(self)
		StackMachine.push(self,temp)
	def mod(self): 
		temp = StackMachine.pop(self) % StackMachine.pop(self)
		StackMachine.push(self,temp)
