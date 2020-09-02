class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True
        is_cap_from_1 = 65 <= ord(word[1]) <= 90
        for i in range(2, len(word)):
            p = word[i-1]
            c = word[i]
            is_cap_p = 65 <= ord(p) <= 90
            is_cap_c = 65 <= ord(c) <= 90
            if is_cap_p != is_cap_c:
                return False
            is_cap_from_1 = is_cap_p
        is_cap_0 = 65 <= ord(word[0]) <= 90
        if is_cap_0 == is_cap_from_1:
            return True
        elif is_cap_0 == True and is_cap_from_1 == False:
            return True
        return False
