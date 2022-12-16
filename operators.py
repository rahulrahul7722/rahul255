a=10
b=a
print(id(a))
print(id(b))
print(a is b)
b=20
print(id(a))
print(id(b))
print(a is b)