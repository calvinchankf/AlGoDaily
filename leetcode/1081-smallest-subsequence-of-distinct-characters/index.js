/*
    1st approach: stack + hashtable
    - similar to leetcode316, 331, 735, 901, 1081
    - first count the number of occurence for each character
    - then we use a stack to store the temp result as we move forward
        - when the current character is lexicographicallly less than stack[-1] and stack[-] still has occurence larger than 0, we pop the stack
    - we push the current character onto the stack
    - we can use a hashtable to indicate which characters are currently in the stack

    Time    O(n)
    Space   O(n)
    88 ms, faster than 57.69%
*/
var smallestSubsequence = function(s) {
    const counts = {}
    for (let c of s) {
        if (c in counts) {
            counts[c] += 1
        } else {
            counts[c] = 1
        }
    }
    const stack = []
    const isUsed = new Set()
    for (let c of s) {
        counts[c] -= 1
        if (isUsed.has(c)) {
            continue
        }
        while (stack.length > 0 && c < stack[stack.length-1] && counts[stack[stack.length-1]] > 0) {
            const pop = stack.pop()
            isUsed.delete(pop)
        }
        stack.push(c)
        isUsed.add(c)
    }
    return stack.join('')
};