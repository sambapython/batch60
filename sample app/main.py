from dbop import insert, browse
while True:
	opt = input("""
	Customer operations:
		1. insert
		2. update
		3. delete
		4. view
		q. quit
		Enter option:""")
	if opt=="q":
		break
	elif opt=="1":
		insert()
	elif opt=="4":
		data = browse()
		print(data)

