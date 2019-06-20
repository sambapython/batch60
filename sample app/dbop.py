import psycopg2
import json
from messages import take_customer_id, take_customer_name,\
operation
f = open("config.json")
db_info = json.load(f)
def get_con():
	con = psycopg2.connect(**db_info)
	cur=con.cursor()
	return con,cur
def browse(c_id=None):
	if not c_id:
		c_id=input(take_customer_id)
	q=f"select * from customer where id={c_id}"
	con,cur=get_con()
	cur.execute(q)
	return cur.fetchall()
def insert():
	c_id=input(take_customer_id)
	name=input(take_customer_name)
	q=f"insert into customer(id,name) values({c_id},'{name}')"
	con,cur=get_con()
	cur.execute(q)
	con.commit()
	print("Customer inserted successfully!!")
	data = browse(c_id)
	print(f"inserted details:{data}")
	con.close()
def update():
	c_id=input(take_customer_id)
	data = browse(c_id)
	if data:
		print(data)
		opt = input(operation)
		opt=opt.casefold()
		if opt=="y":
			c_name = input(take_customer_name)
			q=f"update customer set name='{c_name}' where id={c_id}"
			con,cur=get_con()
			cur.execute(q)
			con.commit()
			print("record updated successfully")
			data = browse(c_id)
			print(data)
			con.close()
		else:
			print("updation cancelled")

	else:
		print("record not found..")
def delete():
	c_id=input(take_customer_id)
	data = browse(c_id)
	if data:
		print(data)
		opt = input(operation)
		opt=opt.casefold()
		if opt=="y":
			q=f"delete from customer where id={c_id}"
			con,cur=get_con()
			cur.execute(q)
			con.commit()
			print("record deleted successfully")
			con.close()
		else:
			print("deletion cancelled")

	else:
		print("record not found..")