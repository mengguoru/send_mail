import json
import ast 

def get_content():
	with open('data.json') as data_file:
		# data= json.load(data_file.read())
		# data = json.loads(s)
		# print(type(data))
		# print(data)
		s = str(data_file.read())
		# print(s)
		# print(type(s))
		dict = ast.literal_eval(s)
		# print(dict)
		# print(dict["content"]["text1"])
		return dict["content"]["text1"]
		
if __name__ == '__main__':
	# print(get_content())
	print(get_content())