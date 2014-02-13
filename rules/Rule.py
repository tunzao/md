class Rule():
	'''
		super rule class
		'''
	def action(self, block, handler):
		handler.start(self.type)
		handler.feed(block)
		handler.end(self.type)
		return True
