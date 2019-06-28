import logging
#logging.info("sdfsd")
#import a
logging.basicConfig(level=logging.DEBUG,
	filename="log.txt",
	format="%(asctime)s==>%(name)s-->%(levelname)s-->%(message)s"
    )

print("welcome")
logging.info("program strted")
a=input("Enter a value:")
logging.debug("A value entered: %s"%a)
b=input("Enter b value:")
logging.debug("B value entered: %s"%b)
logging.debug(f"before conversion a={a},b={b}")
try:
    a=float(a)
    logging.debug("a value converted: %s"%a)
    b=float(b)
    logging.debug("b value converted: %s"%b)
    logging.debug(f"after conversion a={a},b={b}")
    res=a/b
    print("result=",res)
    logging.debug("result: %s"%res)
except ValueError as err:
    print("expecting digits")
    logging.error(err)
except ZeroDivisionError as err:
    print("expecting b!=0")
    logging.error(err)
except Exception as err:
    print("ERROR:",err)
    logging.error(err)
print("thank you!!")
logging.info("program completed.")
print("main block statements....")