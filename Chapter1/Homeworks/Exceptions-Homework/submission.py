a = 12
s = "hello"

try:
	print("inside try")
	print(a + s)
	print("Printed using original data types")
except NameError:
	print("inside except NameError")
	print("One or more of the variables are not defined")
except TypeError:
	print("inside except TypeError")
	print(str(a) + str(s))
	print("Printed using type-casted data types")