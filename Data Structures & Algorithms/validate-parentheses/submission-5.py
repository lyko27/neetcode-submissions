class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return false
        else :
            stack = []
            i = 0
            for i in range(len(s)):
                if s[i] == "(":
                    stack.append(")")
                    j=0
                elif s[i] == "[":
                    stack.append("]")
                    j=0
                elif s[i] == "{":
                    stack.append("}")
                    j=0
                elif s[i] == ")" or s[i] == "]" or s[i] == "}":
                    if stack == [] or s[i] != stack[-1]:
                        return False
                    else:
                        stack.pop()
                i+=1
            if stack == []:
                return True
            else:
                return False

        