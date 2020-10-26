# https://leetcode.com/problems/implement-strstr/


class Solution:

    """
    This function is incorrect. It is only here to understand prior mistakes.
    """
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        if len(haystack) < len(needle):
            return -1
        i = 0
        while i < len(haystack):
            j = 0
            if haystack[i] == needle[j]:
                k = i+1
                j += 1
                while j < len(needle) and k<len(haystack):
                    if haystack[k] == needle[j]:
                        k += 1
                        j += 1
                    else:
                        i += 1
                        break
                if j == len(needle):
                    return i
                else:
                    i += 1
            else:
                i += 1
        return -1

    """
    The upper code is not readable and very difficult to debug.
    A better approach is to limit the loop to the window size which cannot 
    be greater than len(haystack)-len(needle)+1
    
    Also, use slicing which helps to solve the question in only a single loop
    """
    def betterApproach(self, haystack, needle):
        h_len, n_len = len(haystack), len(needle)

        if not needle or needle == "":
            return 0
        if h_len<n_len:
            return -1
        if h_len == n_len:
            return 0 if haystack == needle else -1

        for start_idx in range(h_len-n_len+1):
            n_ptr = 0
            for window_idx in range(start_idx, start_idx+n_len):
                if haystack[window_idx] == needle[n_ptr]:
                    n_ptr += 1
            if n_ptr == n_len:
                return start_idx
        return -1

    def slidingWindow(self, haystack, needle):
        h_len, n_len = len(haystack), len(needle)

        if not needle or needle == "":
            return 0
        if h_len < n_len:
            return -1
        if h_len == n_len:
            return 0 if haystack == needle else -1

        h_ptr = 0

        while h_ptr < h_len-n_len+1:
            while h_ptr < h_len-n_len+1 and haystack[h_ptr] != needle[0]:
                h_ptr += 1

            count, n_ptr = 0, 0
            while n_ptr<n_len and h_ptr<h_len and haystack[h_ptr] == needle[n_ptr]:
                h_ptr += 1
                n_ptr += 1
                count += 1

            if count == n_len:
                return h_ptr - n_len

            h_ptr = h_ptr - count + 1

        return -1





if __name__ == "__main__":
    obj = Solution()
    print(obj.betterApproach(haystack="hello", needle="ll"))
    print(obj.betterApproach(haystack="mississipi", needle="issip"))
    print(obj.betterApproach(haystack="mississippi", needle="issipi"))
    print(obj.betterApproach(haystack="mississippi", needle="pi"))
    print(obj.slidingWindow(haystack="hello", needle="ll"))
    print(obj.slidingWindow(haystack="mississipi", needle="issip"))
    print(obj.slidingWindow(haystack="mississippi", needle="issipi"))
    print(obj.slidingWindow(haystack="mississippi", needle="pi"))


