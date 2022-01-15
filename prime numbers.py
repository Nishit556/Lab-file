def Prime_no():
    lst = []

    N = int(input("Enter N:"))

    for i in range(2, 1000):
        Prime = 1
        for j in range(2, i):  # Divisor
            if (i % j == 0):
                Prime = 0
            else:
                continue
        if Prime == 1:
            lst.append(i)
            if len(lst) == N:
                break
    print(lst)
    print("----------------------------------------")
    print("Program by Nishit Gautam, 0832CS191114")


Prime_no()


