import requests

url = 'http://localhost:3000/testapi'

response = requests.get(url, stream=True)
if not response.ok:
	print "wrong"
	# Something went wrong
else:
	condis = response.headers['content-disposition']
	idx = condis.index('filename=')
	filename = condis[idx+9:]

	with open(filename, 'wb') as handle:
		for block in response.iter_content(1024):
			handle.write(block)


# with open('output.py', 'wb') as handle:
# 	response = requests.get(url, stream=True)
# 	if not response.ok:
# 		print "wrong"
# 		# Something went wrong
# 	else:
# 		for block in response.iter_content(1024):
# 			handle.write(block)


