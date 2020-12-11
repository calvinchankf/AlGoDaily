/*
    Given an int n. You can use only 2 operations:

    - multiply by 2
    - divide by 3 (e.g. 10 / 3 = 3)
    Find the minimum number of steps required to generate n from 1.

    Example 1:

    Input: 10
    Output: 6
    Explanation: 1 * 2 * 2 * 2 * 2 / 3 * 2
    6 steps required, as we have used 5 multiplications by 2, and one division by 3.
    Example 2:

    Input: 3
    Output: 7
    Explanation: 1 * 2 * 2 * 2 * 2 * 2 / 3 / 3
    7 steps required, as we have used 5 multiplications by 2 and 2 divisions by 3.

    ref:
    - https://leetcode.com/discuss/interview-question/406663/Bloomberg-or-Phone-Screen-or-Min-Steps-to-Generate-Number
*/
const minStepsToReachOne = (target) => {
    const seen = new Set()
    const q = [[1, 0]]
    while (q.length > 0) {
        const [x, steps] = q.shift()
        if (x === target) {
            return steps
        }
        if (seen.has(x)) {
            continue
        }
        seen.add(x)
        q.push([x*2, steps + 1])
        q.push([Math.floor(x/3), steps + 1])
    }
    return -1
}

console.log(minStepsToReachOne(10))
console.log(minStepsToReachOne(3))