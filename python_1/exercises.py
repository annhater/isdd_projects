print (9/4)
print (23/5)
print (21/8)
print (7/2)
print (9//4)
print(9%4)
print (23//5)
print(23%5)
print (21//8)
print(21%8)
print (7//2)
print(7%2)

a, b = 9, 4
print(f"{a}/{b} = {a//b} + {a%b}")
a, b = 23, 5
print(f"{a}/{b} = {a//b} + {a%b}")

# list of pairs (a, b)
fractions = [(9, 4), (23, 5), (21, 8), (7, 2)]

for a, b in fractions:
    print(f"{a}/{b} = {a//b} + {a%b}")







