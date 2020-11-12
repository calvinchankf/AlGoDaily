from math import *

"""
    https://leetcode.com/discuss/interview-question/924314/

    Last seen: 4th November 2020, Role: Experience, Location: EU, Medium: HackerRank

    Amazon Cloud Instances
    1.1 Coding exercise
    (see below)

    1.2 Coding approach
    Describe your approach to coding the solution
    Describe the run time complexity of your solution
    Introduction
    Amazon monitors the average utilization of cloud instances for services every second in order to adopt instances based on demand.

    If average utilization in the past second is below 25%, it performs the action to half the number of instances running taking the ceiling if the half does not represent an integer. If the number of instances equals one, do nothing.

    If the avg. utilization is between 25%-65%, do nothing.

    Finally, if the average utilization is above 65%, perform the action of doubling the number of instances if the number of instances does not exceed 2*10^8.

    Every time an action is performed, the following 10 seconds are ignored.

    Example

    averageUtil: [24, 25, 5, 6, 7, 10, 80, 5, 12, 16, 34, 27, 17, 50]
    instances: 2
    The average utilization of the first second is below 25%, no action is performed (averageUtil[0] < 25).

    The following average utilization is between 25% and 65% (25 <= averageUtil[1] <= 65), therefore instances are halved: 2/2 = 1.

    After performing the action, the function does not regard the utilization of the following ten seconds (averageUtil[2] - averageUtil[11]).

    averageUtil[12] is below 25%, however since instances == 1, it does nothing.

    The last element of the input list is 25 <= averageUtil[13] <= 65 and it does nothing.

    Afterwards, there are no more values to consider and the function returns the current number of instances.

    Expected Output: 1

    Function Description
    Complete the xxx (name forgotten) function in the editor below. The function must return an integer that describes the final number of active instances.

    The function has two parameters:

    averageUtil: A list of n integers i
    instances: An integer of current active instances
"""


def f(averageUtil, instances):
    i = 0
    while i < len(averageUtil):
        if averageUtil[i] < 25 and instances > 1:
            instances = int(ceil(instances/2.0))
            i += 10
        elif averageUtil[i] > 65 and instances*2 <= 2*(10**8):
            instances *= 2
            i += 10
        i += 1
    return instances


# 1
a = [24, 25, 5, 6, 7, 10, 80, 5, 12, 16, 34, 27, 17, 50]
b = 2
print(f(a, b))

# 2
a = [5, 10, 80]
b = 1
print(f(a, b))

# 3
a = [30, 5, 4, 8, 19, 89]
b = 5
print(f(a, b))
