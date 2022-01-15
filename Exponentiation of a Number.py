x=int(input("Enter number: "))
y=int(input("Enter power: "))
r=1
for i in range(y):
    r=r*x
z=x**y
if(r==z):
    print("exponential=",r)

print("----------------------------------------")
print("Program by Nishit Gautam, 0832CS191114")
