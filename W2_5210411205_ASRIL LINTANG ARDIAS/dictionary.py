#dictionary
d={1:100, 2:200, 3:300, 4:400, 5:500}
print(d)
print(d[2])
print(d.get(4))
print(d.keys())
print(d.values())
del d[1]
print(d)
b=d.copy()
print(b)
d.clear()
print(d)
len(d)