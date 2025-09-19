#   242 - Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# hashmap both strings
# check if they are the same
# return true if same, else false

        if len(s) != len(t):
            return False
        mapS, mapT = {}, {}

        for character in s:
            mapS[character] = 1 + mapS.get(character, 0)
        for character in t:
            mapT[character] = 1 + mapT.get(character, 0)
        
        return mapS == mapT