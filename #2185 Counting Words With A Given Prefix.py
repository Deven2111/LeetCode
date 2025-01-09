#2185. Counting Words With a Given Prefix
#You are given an array of strings words and a string pref. Return the number of strings in words that contain pref as a prefix. A prefix of a string s is any leading contiguous substring of s.

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(words)
        count = 0
        for i in range(n):
            str1 = words[i]
            if len(pref) > len(str1):
                continue
            if str1.startswith(pref):
                count +=1
        return count