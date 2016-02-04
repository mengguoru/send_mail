import json

def get_content():
	with open('test.json') as data_file:
		data= json.load(data_file)

	# print(data)
	return data['showapi_res_body']['contentlist'][0]['text']

if __name__ == '__main__':
	print(get_content())