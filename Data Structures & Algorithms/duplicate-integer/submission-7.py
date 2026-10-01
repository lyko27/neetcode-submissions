class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Dictionarry_occurency = {}
        if (nums == []):
            return False
        else:
            for i in range(len(nums)):
                if (nums[i] in Dictionarry_occurency):
                    return True
                else :
                    Dictionarry_occurency[nums[i]] = 1
            return False
