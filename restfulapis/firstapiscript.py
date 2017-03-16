import requests 
'''Notice that the requests module has a function called
	'get' that does an HTTP GET. 
'''
resp = requests.get('https://todolist.example.com/tasks/')

if resp.status_code != 200:
	#This means something went wrong.
	raise ApiError('GET /tasks/ {}'.format(resp.status_code))
'''The response object has a method called 'json' 
	that takes the response body from the server
	and transforms it to a Python ist of dictionaries.
	Similar to json.loads()
'''
for todo_item in resp.json():
	print('{} {}'.format(todo_item['id'], todo_item['summary']))

task = {"summary":"Take out trash","description":""}
'''requests provides a function called 'post' which
	does an HTTP POST. It takes a 'json' argument 
	whose value here is a python dictionary. 
	Since we are using json as our data format, 
	we are able to take a shortcut and send the json
	argument to post. This works like json.dumps and sets
	the requests' content type to application/json'''
resp = requests.post('https://todolist.example.com/tasks/', json=task)
'''Per the api spec and REST best practices, we know the
	task is created because of the 201 response code.'''
if resp.status_code != 201:
	raise ApiError('POST /tasks/ {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()["id"]))