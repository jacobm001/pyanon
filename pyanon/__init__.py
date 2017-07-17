import csv
import random

class Anon():
	known_values = {}

	def __init__(*args, **kwds):
		self = args[0]
		args = args[1:]

	def __set__(self, obj, type=None):
		return

	def __getitem__(self, key):
		if key in self.known_values:
			return self.known_values[key]

		else:
			return self.gen_new_value(key)

	def __str__(self):
		return str(self.known_values)
		
	def gen_new_value(self, key):
		while 1:
			value = random.randint(0, 1000000)
			
			if value not in self.known_values.values():
				self.known_values[key] = value
				return value

	def save_relation(self, filename):
		with open(filename, 'w') as csvfile:
			writer = csv.writer(csvfile)

			for key, value in self.known_values.items():
				writer.writerow([ key, value ])