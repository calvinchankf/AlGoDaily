/*
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

    ref:
    - https://leetcode.com/discuss/interview-question/380650/Bloomberg-or-Phone-Screen-or-Candy-Crush-1D
*/
const candy_crush_1d = s => {
    const stack = []
    for (let c of s) {
        if (stack.length > 0 && stack[stack.length-1][0] == c) {
            stack[stack.length-1][1] += 1
        } else {
            if (stack.length > 0 && stack[stack.length-1][1] >= 3) {
                stack.pop()
            }
            if (stack.length > 0 && stack[stack.length-1][0] == c) {
                stack[stack.length-1][1] += 1
            } else {
                stack.push([c, 1])
            }
        }
    }
    if (stack.length > 0 && stack[stack.length-1][1] >= 3) {
        stack.pop()
    }
    let res = ''
    for (let [c, f] of stack) {
        res += c.repeat(f)
    }
    return res
}

a = 'aaaabbbc'  // c
console.log(candy_crush_1d(a))

a = 'aabbbacd'  // cd
console.log(candy_crush_1d(a))

a = 'aabbccddeeedcba'  // (empty)
console.log(candy_crush_1d(a))

a = 'aaabbbacd'  // acd <- would be 'cd' if it is not greedy from left to right
console.log(candy_crush_1d(a))

a = 'baaabbbabbccccd'  // abbd
console.log(candy_crush_1d(a))

console.log("-----")

a = 'bbbbbbb'   // (empty)
console.log(candy_crush_1d(a))

a = 'ccddccdcaacabbbaaccaccddcdcddd'  // (empty)
console.log(candy_crush_1d(a))

a = 'aabbccdddcbax'  // x
console.log(candy_crush_1d(a))

a = 'AABBCCCCDD'  // AABBDD
console.log(candy_crush_1d(a))

a = 'AABBCCCCBADD'  // DD
console.log(candy_crush_1d(a))

a = 'ABBBCC'  // ACC
console.log(candy_crush_1d(a))

a = 'ABCCCBB'  // A
console.log(candy_crush_1d(a))