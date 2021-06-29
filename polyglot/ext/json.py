import json
import os

class JsonStore(object):
	def __init__(self, filename, database_name):
		self.file = filename
		self.name = database_name.strip()
		self.path = os.path.join(os.path.dirname(self.file), f"{self.name}.json")

		assert len(self.name) > 0, "Name should have atleast one character"
		self.store = self.initialize_database()
		print(self.store)

	def initialize_database(self):
		if not os.path.isfile(self.path):
			with open(self.path, "w") as file_writer:
				file_writer.write(json.dumps([]))
				return []
		return self.__get_store_content()

	def __get_store_content(self):
		with open(self.path, "r") as file_reader:
			try:
				return json.loads(file_reader.read())
			except Exception as exception:
				with open(self.path, "w") as file_writer:
					file_writer.write(json.dumps([]))
				return []