"""
    From:
    - https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=288738
    - https://leetcode.com/discuss/interview-question/762546/

    1st approach: 2 pointers
    1. 1st pointer for iterating through the shopping cart
    2. 2nd pointer for looking for the codeLists' list(from the first codeList)
    3. if there is a match between a subarray and a codeList, look for the next codeList(by incrementing the codeList pointer)
    4. if we completely traverse all the codeLists, the 2nd pointer should point to the end of the codeLists
"""


def checkWinner(codeList, shoppingCart):

    # # approach 1
    # if len(codeList) == 0:
    #     return 1
    # if len(shoppingCart) == 0:
    #     return 0
    # codeIdx = 0
    # i = 0
    # while i < len(shoppingCart):
    #     matchCnt = 0
    #     i2 = i
    #     targetArr = codeList[codeIdx]
    #     for j in range(len(targetArr)):
    #         if i2 < len(shoppingCart) and (targetArr[j] == shoppingCart[i2]\
    #             or targetArr[j] == "anything"):
    #             matchCnt += 1
    #             i2 += 1
    #         else:
    #             break
    #     if matchCnt == len(targetArr):
    #         codeIdx += 1
    #         i += len(targetArr)
    #     else:
    #         i += 1
    # return codeIdx == len(codeList)

    # approach 2
    if len(codeList) == 0:
        return 1
    if len(shoppingCart) == 0:
        return 0

    i = 0  # codeList
    j = 0  # shoppingCart
    while i < len(codeList) and j + len(codeList[i]) <= len(shoppingCart):
        matchCount = 0
        codes = codeList[i]
        for k in range(len(codes)):
            if codes[k] == 'anything' or codes[k] == shoppingCart[j+k]:
                matchCount += 1
            else:
                break
        # if we codeList[i] des matches part of the shoppingCart
        if matchCount == len(codes):
            i += 1
            j += len(codes)
        else:
            j += 1
    return i == len(codeList)


print("--- tests from 1p3a ---")

# true
codeList = [
    ["apple", "apple"],
    ["orange", "banana", "orange"],
]
shoppingCart = ["orange", "apple", "apple", "orange", "banana", "orange"]
print(checkWinner(codeList, shoppingCart))

# true
codeList = [
    ["apple", "apple"],
    ["orange", "anything", "orange"],
]
shoppingCart = ["orange", "apple", "apple", "orange", "banana", "orange"]
print(checkWinner(codeList, shoppingCart))

# false
codeList = [
    ["orange", "banana", "orange"],
    ["apple", "apple"],
]
shoppingCart = ["orange", "apple", "apple", "orange", "banana", "orange"]
print(checkWinner(codeList, shoppingCart))

# false
codeList = [
    ["apple", "apple"],
    ["orange", "banana", "orange"],
    ["pear", "orange", "grape"],
]
shoppingCart = [
    "orange", "apple", "apple", "orange", "banana", "orange", "pear", "grape"
]
print(checkWinner(codeList, shoppingCart))

# true
codeList = [
    ["apple", "apple"],
    ["orange", "banana", "orange"],
    ["pear", "orange", "grape"],
]
shoppingCart = [
    "orange", "apple", "apple", "orange", "banana", "orange", "pear", "orange",
    "grape"
]
print(checkWinner(codeList, shoppingCart))

# true
codeList = [
    ["apple", "apple"],
    ["orange", "anything", "orange"],
]
shoppingCart = ["orange", "apple", "apple", "orange", "mango", "orange"]
print(checkWinner(codeList, shoppingCart))

# false
codeList = [
    ["apple", "apple"],
    ["orange", "banana", "orange"],
]
shoppingCart = ["orange", "apple", "apple", "mango", "orange"]
print(checkWinner(codeList, shoppingCart))

print("--- tests from leetcode ---")

codeList = [
    ['apple', 'apple'],
    ['banana', 'anything', 'banana']
]
shoppingCart = ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']
print(checkWinner(codeList, shoppingCart))

codeList = [
    ['apple', 'apple'],
    ['banana', 'anything', 'banana']
]
shoppingCart = ['banana', 'orange', 'banana', 'apple', 'apple']
print(checkWinner(codeList, shoppingCart))

codeList = [
    ['apple', 'apple'],
    ['banana', 'anything', 'banana']
]
shoppingCart = ['apple', 'banana', 'apple', 'banana', 'orange', 'banana']
print(checkWinner(codeList, shoppingCart))

codeList = [
    ['apple', 'apple'],
    ['apple', 'apple', 'banana']
]
shoppingCart = ['apple', 'apple', 'apple', 'banana']
print(checkWinner(codeList, shoppingCart))
