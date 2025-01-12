#2116. Check if a Parentheses String Can Be Valid
#A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true: It is (). It can be written as AB (A concatenated with B), where A and B are valid parentheses strings. It can be written as (A), where A is a valid parentheses string. You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked, If locked[i] is '1', you cannot change s[i]. But if locked[i] is '0', you can change s[i] to either '(' or ')'. Return true if you can make s a valid parentheses string. Otherwise, return false.

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        length = len(s)
        if length % 2 == 1:
            return False
        openBrackets = []
        unlocked = []

        for i in range(length):
            if locked[i] == "0" :
                unlocked.append(i)
            elif s[i] == "(":
                openBrackets.append(i)
            elif s[i] == ")":
                if openBrackets:
                    openBrackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        while openBrackets and unlocked and openBrackets[-1] < unlocked[-1]:
            openBrackets.pop()
            unlocked.pop()
        if openBrackets:
            return False

        return True