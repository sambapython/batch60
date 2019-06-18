import psycopg2
import json
from messages import take_customer_id, take_customer_name
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
	pass
def delete():
	pass