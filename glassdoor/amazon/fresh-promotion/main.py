"""
    From:
    - https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=288738
    - https://leetcode.com/discuss/interview-question/932920/

    Amazon Fresh is running a promotion in which customers receive prizes for purchasing a secret combination of fruits. 
    The combination will change each day, and the team running the promotion wants to use a code list to make it easy to change the combination. 
    The code list contains groups of fruits. Both the order of the groups within the code list and the order of the fruits within the groups matter. 
    However, between the groups of fruits, any number, and type of fruit is allowable. 
    The term "anything" is used to allow for any type of fruit to appear in that location within the group.

    Consider the following secret code list: [[apple, apple], [banana, anything, banana]]
    Based on the above secret code list, a customer who made either of the following purchases would win the prize:
    orange, apple, apple, banana, orange, banana
    apple, apple, orange, orange, banana, apple, banana, banana

    Write an algorithm to output 1 if the customer is a winner else output 0.

    Input:
    The input to the function/method consists of two arguments:
    codeList, a list of lists of strings representing the order and grouping of specific fruits that must be purchased in order to win the prize for the day.
    shoppingCart, a list of strings representing the order in which a customer purchases fruit.

    Output:
    Return an integer 1 if the customer is a winner else return 0.

    Note:
    - 'anything' in the codeList represents that any fruit can be ordered in place of 'anything' in the group.
    - 'anything' has to be something, it cannot be "nothing".
    - 'anything' must represent one and only one fruit.
    - If secret code list is empty then it is assumed that the customer is a winner.

    Example 1:

    Input: codeList = [[apple, apple], [banana, anything, banana]], shoppingCart = [orange, apple, apple, banana, orange, banana]
    Output: 1
    Explanation:
    codeList contains two groups - [apple, apple] and [banana, anything, banana].
    The second group contains 'anything' so any fruit can be ordered in place of 'anything' in the shoppingCart. 
    The customer is a winner as the customer has added fruits in the order of fruits in the groups and the order of groups in the codeList is also maintained in the shoppingCart.

    Example 2:

    Input: codeList = [[apple, apple], [banana, anything, banana]], shoppingCart = [banana, orange, banana, apple, apple]
    Output: 0
    Explanation:
    The customer is not a winner as the customer has added the fruits in order of groups but group [banana, orange, banana] is not following the group [apple, apple] in the codeList.

    Example 3:

    Input: codeList = [[apple, apple], [banana, anything, banana]], shoppingCart = [apple, banana, apple, banana, orange, banana]
    Output: 0
    Explanation:
    The customer is not a winner as the customer has added the fruits in an order which is not following the order of fruit names in the first group.

    Example 4:

    Input: codeList = [[apple, apple], [apple, apple, banana]], shoppingCart = [apple, apple, apple, banana]
    Output: 0
    Explanation:
    The customer is not a winner as the first 2 fruits form group 1, all three fruits would form group 2, but can't because it would contain all fruits of group 1.
"""


def checkWinner(codeList, shoppingCart):
    """
        1st approach: 2 pointers
        1. 1st pointer for iterating through the shopping cart
        2. 2nd pointer for looking for the codeLists' list(from the first codeList)
        3. if there is a match between a subarray and a codeList, look for the next codeList(by incrementing the codeList pointer)
        4. if we completely traverse all the codeLists, the 2nd pointer should point to the end of the codeLists
    """

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
        # if the codeList[i] matches part of the shoppingCart
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
