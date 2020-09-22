"""
primitive string will have equal number of characters (here parenthesis).
We print everything b/w left most i.e fist ( and right most i.e last )
"""
s = "(()())(())(()(()))"  # ans ()()()()(())
result = []
opened = 0

for c in s:
    if c == "(" and opened > 0:
        result.append(c)
    if c == ")" and opened > 1:
        result.append(c)
    opened += 1 if c == "(" else -1
print(''.join(result))
