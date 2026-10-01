class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Dictionarry_occurency = {}
        if (List == []):
            return True
        else:
            for i in range(len(List)):
                if (List[i] in Dictionary_occurency):
                    return True
                else :
                    Dictionary_occurency[List[i]] = 1
            return False
