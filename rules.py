class Rule:
	"""
	super class of Rule
	"""
	def action(self, block, handler):
		handler.start(self.type)
		handler.feed(block)
		handler.end(self.type)
		return True

class HeadingRule(Rule):
	"""
	标题是一个最多70个字符的行，不以冒号结束
	"""
	type = "heading"
	def condition(self, block):
		return "\n" not in block and len(block) <= 70
		and not block[-1] == ":"

class TitleRule(Rule):
	"""
	题目是文档的第一个快，作为标题存在
	"""
	type = "title"
	first = True

	def condition(self, block):
		if not self.first return False
		self.first = False
		#todo 好吧，这个语法我还不太清楚
		return HeadingRule.condition(self, block)

class ListItemRule(Rule):
	"""
	列表是以连字符作为开始的段落，最为格式化的一部分，连字符被剔除
	"""
	type = "listitem"

	def condition(self, block):
		return block[0] == "-"

	def action(self, block, handler):
		handler.start(self.type)
		handler.feed(block[1:].strip())
		handler.end(self.type)
		return True

class List(ListItemRule):
	"""
	列表开始于并非列表的块和随后的列表块之间,由最后一个连续块作为结束
	"""

	type = "list"
	inside = False

	def condition(self, block):
		return True

	def action(self, block, handler):
		if not self.inside and ListItemRule.condition(self, block):
			handler.start(self.type)
			self.inside = True
		elif self.inside and not ListItemRule.condition(self, block):
			handler.end(self.type)
			self.inside = False
		return False


class ParagrapRule(Rule):
	"""
	默认规则，处理所有未被其他规则处理的段落
	"""

	type = "paragraph"

	def condition(self, block):
		return True
	
	
