def newtonSqrt(n, base):
    approx_root = 0.5 * n
    for i in range(base):
        betterapprox = 0.5 * (approx_root + n/approx_root)
        approx_root = betterapprox
    return betterapprox

print("the square root of 100 :",newtonSqrt(100, 10))
print("the square root of 256 :",newtonSqrt(256, 10))
print("the square root of 24 :",newtonSqrt(24, 10))

print("----------------------------------------")
print("Program by Nishit Gautam, 0832CS191114")