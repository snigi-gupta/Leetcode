commands = ["GGGGGLGGRG", "R"]
instruction = "GGGGGLGGRG"
def fun(instruction):
    if  instruction == '':
        return True
    if 'G' not in instruction:
        return True
    while 'R' in instruction:
        instruction = instruction.replace('R','LLL')
    while 'LLLL' in instruction:
        instruction = instruction.replace('LLLL','')
    dri = [0,1]
    pos = [0,0]
    d = {'[0,1]':[-1,0], '[-1,0]':[0,-1], '[0,-1]':[1,0],'[1,0]':[0,1]}
    for s in instruction*4:
        if s == 'L':
            key = str(dri).replace(' ','')
            dri = d[key]
        else:
            pos = [pos[0]+dri[0], pos[1]+dri[1]]
    if pos == [0,0]:
        return True
    return False


print(fun(instruction))


# if "L" not in instructions and "R" not in instructions:
#     print(False)
# mapp = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# dirc = 0
# pos = [0, 0]
# for ins in instructions:
#     if ins == "G":
#         pos[0] += mapp[dirc][0]
#         pos[1] += mapp[dirc][1]
#     if ins == "L":
#         dirc = dirc - 1 if dirc > 0 else 3
#     elif ins == "R":
#         dirc = dirc + 1 if dirc < 3 else 0
#
# if pos == [0, 0] or dirc != 0:
#     print(True)
# print(True)


# all_outputs = []
# for test_case in commands:
#     dir_x, dir_y = 0,0
#     delta_x, delta_y = 0,1
#
#     for i in test_case:
#         if i == 'R':
#             delta_x, delta_y = delta_y, delta_x
#         if i == 'L':
#             delta_x, delta_y = -delta_y, delta_x
#         if i == 'G':
#             dir_x, dir_y= dir_x+delta_x, dir_y+delta_y
#
#         answer = (dir_x, dir_y) == (0,0) or (delta_x,delta_y) != (0,1)
#
#     if answer:
#         all_outputs.append("YES")
#     else:
#         all_outputs.append("NO")
# print(all_outputs)