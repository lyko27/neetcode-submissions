class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Dictionarry_occurency = {}
        if (nums == []):
            return false
        else:
            for i in range(len(nums)):
                if (nums[i] in Dictionarry_occurency):
                    return true
                else :
                    Dictionarry_occurency[nums[i]] = 1
            return False
