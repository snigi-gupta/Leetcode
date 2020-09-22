n = 234 #ans = 15

n_str = str(n)

n_prod = 1
n_sum = 0
for num in n_str:
    n_prod *= int(num)
    n_sum += int(num)

print(n_prod - n_sum)
