import re
from util import blocks

class Parser:
	def __init__(self, handler) :
		self.handler = handler
		self.filters = [] 	# 每个filter都是一个函数
		self.rules = []

	def addRule(self, rule) :
		self.rules.append(rule)

	def addFilter(self, pattern, name):
		def filter(block, handler):
			return re.sub(pattern, handler.sub(name), block)
		self.filters.append filter)

	def parse(self, file):
		self.handler.start("document")
		for block in blocks(file):
			for filter in self.filters:
				block = filter(block, self.handler)
			for rule in self.rules:
				if rule.condition(blokc):
					last = rule.action(block, self.handler)
					if last break
		self.handler.end("document")
