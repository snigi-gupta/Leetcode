
def getSubArrays(a, n):
    allSubArrays = []
    for i in range(len(a) + 1):
        for j in range(i + 1, len(a) + 1):

            sub = a[i:j]
            allSubArrays.append(sub)

    return allSubArrays

def refineArrays(allSubArrays, c):
    refined = []
    for arr in allSubArrays:
        if len(arr)>=len(c):
            refined.append(arr)
        check = all(item in a for item in c)
        if not check:
            refined.remove(arr)
    return refined

a = [1,1,5,1,2]
b = [1,2]
c = [2,1]
n = len(a)
allSubArrays = getSubArrays(a, n)
print(allSubArrays)
refinedSubArrays = refineArrays(allSubArrays,c)

print(refinedSubArrays)