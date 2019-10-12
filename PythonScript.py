print("Hello World")
x = 20;
y = 2.5;

def addten(param1):
	#do Stuff
	if type(param1) != int:
		print("Not an Integer")
	else:
		print("Integer found")
		return param1 +10

x=addten(x)

y=addten(y)
print(x,y)

a=30
b=4.5


def subThree(param2):
	#do other thing
	if type(param2) !=int :
		print("not an Integer")
	else:
		print("Integer found")
		return param2-3

a=subThree(a)
b=subThree(b)
print(a,b)