x = -123

s = (x > 0) - (x < 0)
r = int(str(x*s)[::-1])
print(s*r * (r < 2**31))

