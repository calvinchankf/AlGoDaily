/*
    - https://leetcode.com/discuss/interview-question/390895/Postman-or-Software-Engineering-Internship-or-Coding-Challenge
    - https://leetcode.com/discuss/interview-question/453354/POSTMAN-or-SWE-Internship-or-Coding-Challenge
    A program generates an output of an array of integers. The programmer forgot to separate the numbers with white-spaces. You have a string S of length N consisting of non-negative integers. All the integers were not greater than C without leading zeroes. Write a program to find how many arrays could have S as an output? The answer can be very large, print it as modulo10^k.
    Input Format
    The first line contains 3 space-separeted integers: N, C, and K.
    The second line contains a string S of length N.
    Output Format
    Output the answer modulo 10^k.
    Input Constraints
    1 <= N <= 100000
    1 <= C <= 10^9
    1 <= k <= 18
    Sample Input
    7 1234567 9
    1234567
    
    Sample Output
    64
*/

/*
    similar to lc91
*/
const f = (S, C, K) => {
    return dfs(S, C, K, {})
}
const dfs = (S, C, K, ht) => {
    if (S.length == 0) {
        return 1
    }
    if (S in ht) {
        return ht[S]
    }
    let total = 0
    for (let i = 0; i < S.length; i++) {
        const numStr = S.slice(0, i+1)
        const remain = S.slice(i+1, S.length)
        const num = parseInt(numStr)
        if (`${num}` == numStr && num <= C) {
            total += dfs(remain, C, K, ht)
            total %= 10**K
        }
    }
    ht[S] = total
    return total
}

/*
    expect: 64
*/
let a = '1234567'
let b = 1234567
let c = 9
console.log(f(a, b, c))

/*
    expect: 3
    1,2,0,4
    12,0,4
    1,20,4
*/
a = '1204'
b = 32
c = 9
console.log(f(a, b, c))

/*
    expect: 2
    1,2,3
    12,3
*/
a = '123'
b = 12
c = 7
console.log(f(a, b, c))