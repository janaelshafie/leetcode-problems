#general solution to all inputs including unicode characters
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        for char in t:
            if char not in count:
                return False
            count[char] -= 1

            if count[char] < 0:
                return False

        return True

        


        