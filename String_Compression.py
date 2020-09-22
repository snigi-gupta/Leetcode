class Solution:
    def compress(self, chars):
        i = 0
        j = i+1
        len_str = len(chars)
        compressed_str = ""
        flag = False
        # while j < len_str or flag:
        #     if j == len_str or chars[i] != chars[j]:
        #         compressed_str += chars[i]
        #         if flag:
        #             compressed_str += str(j-i)
        #             flag = False
        #         i = j
        #         j += 1
        #     else:
        #         j += 1
        #         flag = True

        while j < len_str or flag:
            if j == len_str or chars[i] != chars[j]:
                compressed_str += chars[i]
                if flag:
                    compressed_str += str(j-i)
                    flag = False
                i = j
                j += 1
            else:
                j += 1
                flag = True

        if j == len_str:
            compressed_str += chars[len_str-1]
        return compressed_str




if __name__ == "__main__":
    chars_list = ["abaabass", "aabbccc", "abbbbbbbbbbbb", "aaabaaaaccaaaaba", ""]

    obj = Solution()
    for chars in chars_list:
        print(chars)
        print(obj.compress(chars))
