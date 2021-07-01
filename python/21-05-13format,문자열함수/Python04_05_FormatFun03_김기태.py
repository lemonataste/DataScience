a = "{2:<10}".format('aa','bb','cc')
b = "{1:>10}".format('aa','bb','cc')
c = "{:^10}".format('aa','bb','cc')
d = "{0:w^10}".format('aa','bb','cc')

print(a)
print(b)
print(c)
print(d)


x = 1232123123
y = 1231.312332
e1 = "{1:0.3f} {0:,d}".format(x,y)
e2 = "{:20.3f}".format(y)

print(e1)
print(e2)