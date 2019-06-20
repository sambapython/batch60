import time
f=open("a.txt","w")
try:
    print("try")
    f.write("try")
    f.flush()
    time.sleep(3000)
except Exception as err:
    print(err)
    f.write("exception........")
    f.flush()
except:
	print("except")
	f.write("except....")
	f.flush()
finally:
    print("finally")
    f.write("finall")
    f.flush()
print("main")