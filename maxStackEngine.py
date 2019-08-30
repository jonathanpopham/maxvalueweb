
class MaxStack:
	def __init__(self):
		self.stack = []
		self.current_max = None

	def push(self, value):
		if not self.current_max
			self.current_max = value
		else:
				self.current_max = max(self.current_max, value)
			self.stack.append((val, self.current_max))

		def pop(self):
			self.stack.pop()

		def max(self):
				return self.stack[len(self.stack)-1][1]