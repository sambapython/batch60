def add(x,y):
	"""
	x=10, y=20: 30
	x=s1, y=s2: s1s2
	x=s1, y=20: None
	x=10, y=s2: None
	"""
	try:
		return x+y
	except:
		return None