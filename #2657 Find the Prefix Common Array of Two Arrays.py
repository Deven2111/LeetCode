#2657. Find the Prefix Common Array of Two Arrays
#You are given two 0-indexed integer permutations A and B of length n. A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B. Return the prefix common array of A and B. A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        C = [0] * n
        for currentIndex in range(n):
            commonCount = 0
            for aIndex in range(currentIndex+1):
                for bIndex in range(currentIndex+1):
                    if A[aIndex] == B[bIndex]:
                        commonCount +=1
                        break
            C[currentIndex] = commonCount
        return C