# https://leetcode.com/problems/shuffle-string/
class Soluton:
    def restoreString(self, s, indices):
        result = ["" for _ in range(len(s))]
        for x, i in enumerate(indices):
            result[i] = s[x]
        return ''.join(result)


if __name__ == "__main__":
    obj = Soluton()
    print(obj.restoreString(s="codeleet", indices=[4,5,6,7,0,2,1,3]))