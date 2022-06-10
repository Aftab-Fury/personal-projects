print("welcome to tip calc")
a = float(input("what was the total bill?"))
b =float(input("how many peopel"))
c = float(input('what percentage would u like to tip?'))


d = a+c
e = d/b
x= "{:.2f}".format(e)
print("each person should pay",x)