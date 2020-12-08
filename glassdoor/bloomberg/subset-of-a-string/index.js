/*
    https://leetcode.com/discuss/interview-question/439548/Bloomberg-Phone-Interview-Questions

    e.g. String "abc" should output
    empty string
    a
    b
    c
    ab
    bc
    ac
    abc
*/
const subsetsOfString = (s) => {
    const res = []
    const dfs = (remain, chosen) => {
        res.push(chosen)
        for (let i = 0; i < remain.length; i++) {
            const _remain = remain.slice(i+1)
            const _chosen = chosen + remain[i]
            dfs(_remain, _chosen)
        }
    }
    dfs(s, '')
    return res
}

let a

a = 'abc'
console.log(subsetsOfString(a))

a = 'wxyz'
console.log(subsetsOfString(a))