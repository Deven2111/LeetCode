#2683. Neighboring Bitwise XOR
#A 0-indexed array derived with length n is derived by computing the bitwise XOR (⊕) of adjacent values in a binary array original of length n. Specifically, for each index i in the range [0, n - 1]: If i = n - 1, then derived[i] = original[i] ⊕ original[0]. Otherwise, derived[i] = original[i] ⊕ original[i + 1]. Given an array derived, your task is to determine whether there exists a valid binary array original that could have formed derived. Return true if such an array exists or false otherwise. A binary array is an array containing only 0's and 1's
#IMP: Since XOR is both commutative and associative, the order doesn’t matter. When all occurrences of original[i] are XORed together, they cancel each other out: original[0] XOR original[0] XOR original[1] XOR original[1] ... = 0
#If the derived array is valid (i.e., it was generated from some original), then the XOR of all elements in derived must be 0. This is because all elements of original cancel out when XORed.

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        XOR = 0
        for element in derived:
            XOR = XOR ^ element
        if XOR == 0:
            return True
        else:
            return False