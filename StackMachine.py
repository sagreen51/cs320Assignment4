class StackMachine:
	def__init__(self):
		self.list = []
	def push(self, list):
		self.list.insert(0,item)
	def pop(self):
		return self.list.pop(0)
	def isEmpty(self):
		return self.list == []
	def peek(self):
		return self.list[0]
	def size(self):
		return len(self.list)
