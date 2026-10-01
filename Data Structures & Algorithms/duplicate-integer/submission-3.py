class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Dictionarry_occurency = {}
        if (nums == []):
            return True
        else:
            for i in range(len(nums)):
                if (nums[i] in Dictionary_occurency):
                    return True
                else :
                    Dictionary_occurency[nums[i]] = 1
            return False
