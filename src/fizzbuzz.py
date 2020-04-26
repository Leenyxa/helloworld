i = 0

while i < 101:
	if (i % 3 == 0):
		out = 'fizz'
	else:
		out = ''
	if (i % 5 == 0):
		out = out + 'buzz'

	if (out == ''):
		print(i)
	else:
		print(out)
	i = i+1
