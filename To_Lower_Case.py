# https://leetcode.com/problems/to-lower-case/
str = "HELLO" #ans hello
new_str = []
for c in str:
    if 65 <= ord(c) <= 90:
        new_str.append(chr(ord(c) + 32))
    else:
        new_str.append(c)
print(''.join(new_str))
