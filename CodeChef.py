test_case = int(input())
while (test_case):
    test_case -= 1

    lst1 = [x for x in input().split()]

    lst2 = [x for x in input().split()]


    def countfunc(x):
        count = 0
        for j in lst1:
            count += 1
            if x == j:
                return [count, x]


    s = set(lst2)
    if 'A' in s:
        countA = countfunc('A')
    else:
        countA = [100, 'A']
    if 'B' in s:
        countB = countfunc('B')
    else:
        countB = [100, 'B']
    if 'C' in s:
        countC = countfunc('C')
    else:
        countC = [100, 'C']

    x = min(countA, countB, countC)
    print(x[1])