import random

class Anon():
	known_values = {}

	def __init__(*args, **kwds):
		self = args[0]
		args = args[1:]

	def anonymize(self, key):
		if key in self.known_values:
			return self.known_values[key]

		else:
			return self.gen_new_value(key)
		
	def gen_new_value(self, key):
		while 1:
			value = random.randint(0, 1000000)
			
			if value not in self.known_values.values():
				self.known_values[key] = value
				return value