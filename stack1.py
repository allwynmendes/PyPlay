class Stack:

	def __init__(self):
		print("__init__ called\n")
 		self.items = []

	def isEmpty(self):
		print("isEmpty called\n")
		return self.items == []

	def push(self, item):
		return self.items.insert(0, item)

	def pop(self):
		return self.items.pop(0)

	def peek(self):
		return self.items[0]

s = Stack()
s.push('hello')
s.push(' world')
print(s.pop())
print(s.pop())
print(s.pop())