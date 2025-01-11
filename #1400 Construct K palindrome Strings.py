#1400. Construct K Palindrome Strings
#Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        freq = [0] * 26
        oddCount = 0

        for ch in s:
            freq[ord(ch)-ord('a')] += 1

        for count in freq:
            if count %2 ==1:
                oddCount += 1
        return oddCount <= k