a=2
b=2
print(a==b)
print(a is b)
print(id(a))
print(id(b))
print(id(a) is id(b))
print(id(a) == id(b))
c=2.0
d=2
print(c==d)
print(c is b)
print(id(c))
print(id(d))
print(id(c) is id(d))
print(id(c) == id(d))

print(id(id(a)))
print(id(id(b)))
