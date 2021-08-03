#method overriding 
class add:
	def result(self,a,b):
		print("addition:",a+b)
		
class multi:
	def result(self,a,b):
		print("multiplication:",a*b)
		
class sub(multi):
	pass
		
m=multi()
m.result(20,10)

k=add()
k.result(20,30)

j=sub()
j.result(40,10)


print("---------------")
class add:
	def result(self,x,y):
		print("addition:",x+y)
		
class multi(add):
	def result(self,a,b):
		super().result(20,30)
		print("multiplication:",a*b)
		
s=multi()
s.result(30,20)