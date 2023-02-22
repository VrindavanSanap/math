def sqrt(x):
    z = x/(1+(x-1)/x)
    for i in range(5):
        z -= (z*z - x) / (2*z)
    return z

n = 234
print(n**0.5)
print(sqrt(n))