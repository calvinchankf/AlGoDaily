/*
    There is a string which only contains 0, 1 and '?', where, ? can be 0 or 1

    Given a string s, console.log all the possibilities.

    e.g.
    Input: '??01'
    Output: ['0001', '0101', '1001', '1101']
*/
const xx01 = (s) => {
    const res = []
    const dfs = (i, cur) => {
        if (i === s.length) {
            res.push(cur)
            return
        }
        if (s[i] == '?') {
            dfs(i+1, cur + '0')
            dfs(i+1, cur + '1')
        } else {
            dfs(i+1, cur + s[i])
        }
    }
    dfs(0, '')
    return res
}

let a

a = '??01'
console.log(xx01(a))

a = '??0?1'
console.log(xx01(a))

a = '?'.repeat(32)
console.log(xx01(a))