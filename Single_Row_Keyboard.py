# https://leetcode.com/problems/single-row-keyboard/
keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode" #ans 73
key_index = {c: i for i, c in enumerate(keyboard)}
# print(key_index)
total = 0
start = 0

for c in word:
    if c in key_index:
        total += abs(key_index[c] - start)
        start = key_index[c]
print(total)