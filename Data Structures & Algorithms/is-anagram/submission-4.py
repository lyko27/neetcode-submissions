class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Dico = {}
        DicoT = {}
        if (s == "" or t == ""):
            return true
        else :
            for i in range(len(s)):
                if (s[i] in Dico) :
                    Dico[s[i]] += 1
                else :
                    Dico[s[i]] = 1
            for j in range(len(t)):
                if (t[j] in DicoT) :
                    DicoT[t[j]] += 1
                else :
                    DicoT[t[j]] = 1
            return Dico == DicoT
        