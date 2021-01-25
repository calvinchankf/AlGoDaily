from collections import defaultdict

"""
    https://leetcode.com/discuss/interview-question/480631/Yelp-or-OA-2020-or-Detect-and-Order-Business

    I recently applied for a SWE internship position at Yelp in the EMEA region. 
    I got a reponse pretty quickly which contained a Hackerrank Test. 
    I got the standard Recommend Business problem but I was unable to complete it and informed the recruiter. 
    She responded the next day with another Hackerrank Test.

    Apparently Yelp has a thing for modelling their questions based on Businesses.

    This problem deals with Chain Businesses i.e businesses that operate in multiple locations.

    The problem was given a list of Buisnesses which are C and a target location return a sorted (ascending) list of Chains. 
    The chains are ordered based on the frequency of occurence. 
    The list can contain duplicate business chains i.e same business name, id and location appearing more than once. 
    We break frequency ties by ordering the chain names alphabetically.
"""


class Business:
    def __init__(self, name, location, bid):
        self.name = name
        self.location = location
        self.bid = bid

# class Chain:
#     def __init__(self, name, freq):
#         self.name = name
#         self.freq = freq


def getChain(businessList, targetLocation):
    chainHt = {}
    for b in businessList:
        name = b.name
        location = b.location
        bid = b.bid
        if location == targetLocation:
            key = name + '-' + str(bid)
            if key in chainHt:
                chainHt[key][1] += 1
            else:
                chainHt[key] = [name, 1]
    freqs = chainHt.values()
    freqs.sort(key=lambda x: (x[1], x[0]))
    return freqs


businessList = []
for _ in range(5):
    businessList.append(Business('coke', 'india', 1))
for _ in range(3):
    businessList.append(Business('coke', 'italy', 1))
for _ in range(4):
    businessList.append(Business('pepsi', 'india', 2))
for _ in range(3):
    businessList.append(Business('pepsi', 'india', 6))
for _ in range(5):
    businessList.append(Business('dabur', 'india', 3))
for _ in range(5):
    businessList.append(Business('raw', 'india', 4))
for _ in range(4):
    businessList.append(Business('pepsi', 'argentina', 2))
print(getChain(businessList, 'india'))
print(getChain(businessList, 'italy'))
print(getChain(businessList, 'argentina'))
