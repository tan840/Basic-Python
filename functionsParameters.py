x = 5
def ScopeTest():
	global x
	print(x)
	print(x+5)
	x+=1
	print(x)

#ScopeTest()

def ArgsTest(*args):
	print (type(args))
	for arg in args:
		print(arg)

#ArgsTest(3,5,"tree")

def argsTest(**kwargs):
	print(type(kwargs))

	print(kwargs)

	for arg in kwargs.items():
		print(arg)


argsTest(x=3, y=5)