class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == []:
            return False
        left = 0
        size = len(s)
        right = size-1
        while (left <= right):
            if s[right].isalnum() and s[left].isalnum():
                if s[right].upper() != s[left].upper():
                    return False
                right -=1
                left +=1
            if right > -1 and not s[right].isalnum():
                right-=1
            if left < size and not s[left].isalnum() :
                left +=1
        return True

