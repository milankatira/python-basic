def my_func():
	x=5
	y=6
	print(x+y)
	return x + y
	
	
a=int(2.0)
b=5
c=a+b

breakpoint()

e=3
f=6
g=e+f

breakpoint()
xy=my_func()
print("done")

#--list of debug command--

'''
read python docs
https://docs.python.org/3/library/pdb.html

some important are
h:help
w:where
n:next
s:step(steps into function)
c:continue
p:print
l:list
q:quit

'''