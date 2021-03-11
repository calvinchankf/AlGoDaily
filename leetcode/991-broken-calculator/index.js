/*
    2nd: math, work backwards greedily, learned from others
    - when current > target, we either /2 to reach to the target(if its an even) OR +1 to reach to the target(if its an odd)
    - after the above, we only do +1 from the current to the target

    ref:
    - https://leetcode.com/problems/broken-calculator/solution/
    - https://leetcode.com/problems/broken-calculator/discuss/234484/JavaC%2B%2BPython-Change-Y-to-X-in-1-Line

    Time    O(logN)
    Space   O(1)
    1184 ms, faster than 6.67%
*/
var brokenCalc = function(X, Y) {
    let steps = 0
    while (Y != X) {
        if (Y > X && Y % 2 == 0) {
            Y /= 2
        } else {
            Y += 1
        }
        steps += 1
    }
    return steps
};