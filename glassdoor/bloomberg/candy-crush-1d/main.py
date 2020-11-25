"""
    Write a function to crush candy in one dimensional board. 
    In candy crushing games, groups of like items are removed from the board. 
    In this problem, any sequence of 3 or more like items should be removed and any items adjacent to that sequence should now be considered adjacent to each other. 
    This process should be repeated as many time as possible. You should greedily remove characters from left to right.

    Example 1:
    
    Input: "aaabbbc"
    Output: "c"
    Explanation:
    1. Remove 3 'a': "aaabbbbc" => "bbbbc"
    2. Remove 4 'b': "bbbbc" => "c"
    
    Example 2:
    
    Input: "aabbbacd"
    Output: "cd"
    Explanation:
    1. Remove 3 'b': "aabbbacd" => "aaacd"
    2. Remove 3 'a': "aaacd" => "cd"
    
    Example 3:

    Input: "aabbccddeeedcba"
    Output: ""
    Explanation:
    1. Remove 3 'e': "aabbccddeeedcba" => "aabbccdddcba"
    2. Remove 3 'd': "aabbccdddcba" => "aabbcccba"
    3. Remove 3 'c': "aabbcccba" => "aabbba"
    4. Remove 3 'b': "aabbba" => "aaa"
    5. Remove 3 'a': "aaa" => ""
    
    Example 4:

    Input: "aaabbbacd"
    Output: "acd"
    Explanation:
    1. Remove 3 'a': "aaabbbacd" => "bbbacd"
    2. Remove 3 'b': "bbbacd" => "acd"
"""


def candy_crush_1d(s):
    stack = []  # (char, count)
    for c in s:
        if len(stack) > 0:
            if stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                if stack[-1][1] >= 3:
                    stack.pop()
                if len(stack) > 0 and stack[-1][0] == c:
                    stack[-1][1] += 1
                else:
                    stack.append([c, 1])
        else:
            stack.append([c, 1])
    if len(stack) > 0 and stack[-1][1] >= 3:
        stack.pop()
    res = ''
    for c, count in stack:
        res += count * c
    return res


print('--- greedy: stack ---')

a = 'aaaabbbc'  # c
print(candy_crush_1d(a))

a = 'aabbbacd'  # cd
print(candy_crush_1d(a))

a = 'aabbccddeeedcba'  # (empty)
print(candy_crush_1d(a))

a = 'aaabbbacd'  # acd <- would be 'cd' if it is not greedy from left to right
print(candy_crush_1d(a))

a = 'baaabbbabbccccd'  # abbd
print(candy_crush_1d(a))

print("-----")

a = 'bbbbbbb'   # (empty)
print(candy_crush_1d(a))

a = 'ccddccdcaacabbbaaccaccddcdcddd'  # (empty)
print(candy_crush_1d(a))

a = 'aabbccdddcbax'  # x
print(candy_crush_1d(a))

a = 'AABBCCCCDD'  # AABBDD
print(candy_crush_1d(a))

a = 'AABBCCCCBADD'  # D
print(candy_crush_1d(a))

print("-----")

a = 'AAABBB'  # (empty)
print(candy_crush_1d(a))

a = 'aaabbba'  #
print(candy_crush_1d(a))

print("--- greedy: recursion ---")


def candy_crush_1d(s):
    left = 0
    for right in range(len(s)+1):
        if right < len(s) and s[left] == s[right]:
            continue
        if right - left >= 3:
            return candy_crush_1d(s[:left] + s[right:])
        else:
            left = right
    return s


a = 'aaaabbbc'  # c
print(candy_crush_1d(a))

a = 'aabbbacd'  # cd
print(candy_crush_1d(a))

a = 'aabbccddeeedcba'  # (empty)
print(candy_crush_1d(a))

a = 'aaabbbacd'  # acd <- would be 'cd' if it is not greedy from left to right
print(candy_crush_1d(a))

a = 'baaabbbabbccccd'  # abbd
print(candy_crush_1d(a))

print("-----")

a = 'bbbbbbb'   # (empty)
print(candy_crush_1d(a))

a = 'ccddccdcaacabbbaaccaccddcdcddd'  # (empty)
print(candy_crush_1d(a))

a = 'aabbccdddcbax'  # x
print(candy_crush_1d(a))

a = 'AABBCCCCDD'  # AABBDD
print(candy_crush_1d(a))

a = 'AABBCCCCBADD'  # D
print(candy_crush_1d(a))

print("-----")

a = 'AAABBB'  # (empty)
print(candy_crush_1d(a))

a = 'aaabbba'  #
print(candy_crush_1d(a))

"""
    Follow-up:
    What if you need to find the shortest string after removal?

    Example:

    Input: "aaabbbacd"
    Output: "cd"
    Explanation:
    1. Remove 3 'b': "aaabbbacd" => "aaaacd"
    2. Remove 4 'a': "aaaacd" => "cd"
"""
