#26. Remove Duplicates from Sorted Array
#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j =1
        for i in range(1,len(nums)):
            if nums[i] != nums[j-1]:
                nums[j] = nums[i]
                j +=1
        return j
