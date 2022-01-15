l=[]
n=int(input("Enter total number of elemnets in the list"))
for i in range(n):
    a=int(input("enter elemnet"))
    l.append(a)
m=l[0]
for i in l:
    if(i>m):
        m=i

print(m)
print("----------------------------------------")
print("Program by Nishit Gautam, 0832CS191114")