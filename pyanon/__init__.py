import csv
import uuid

class Anon():
	known_values = {}

	def __init__(self):
		pass

	def __set__(self, obj, type=None):
		return

	def __getitem__(self, key):
		try:
			return self.known_values[key]
		except KeyError:
			value = uuid.uuid1()
			self.known_values[key] = value
			
			return self.known_values[value]
		
	def save_relation(self, filename):
		with open(filename, 'w') as csvfile:
			writer = csv.writer(csvfile)

			for key, value in self.known_values.items():
				writer.writerow([ key, value ])
