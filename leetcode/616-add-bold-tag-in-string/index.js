/*
    1st: sort + hashtable
    - merge intervals to merge all the bold tag
    - similar to lc56, 452, 616, 758

    Time    O(NlogN)
    Space   O(N)
    96 ms, faster than 67.57%
*/
var addBoldTag = function(S, dict) {
    const intvs = []
    for (let word of dict) {
        let fromIdx = 0
        while (1) {
            const i = S.indexOf(word, fromIdx)
            if (i == -1) { break }
            const s = i
            const e = i + word.length
            intvs.push([s, e])
            fromIdx = s + 1
        }
    }
    if (intvs.length == 0) {
        return S
    }
    // merge intervals
    intvs.sort((a, b) => {
        if (a[0] == b[0]) {
            return a[1] - b[1]
        }
        return a[0] - b[0]
    })
    const mergeds = [intvs[0]]
    for (let i = 1; i < intvs.length; i++) {
        const [s, e] = intvs[i]
        const n = mergeds.length
        if (s <= mergeds[n-1][1]) {
            mergeds[n-1][1] = Math.max(mergeds[n-1][1], e)
        } else {
            mergeds.push([s, e])
        }
    }
    // generate the result
    const starts = new Set()
    const ends = new Set()
    for (let [s, e] of mergeds) {
        starts.add(s)
        ends.add(e)
    }
    let res = ''
    for (let i = 0; i < S.length + 1; i++) {
        if (ends.has(i)) {
            res += '</b>'
        }
        if (starts.has(i)) {
            res += '<b>'
        }
        if (i < S.length) {
            res += S[i]
        }
    }
    return res
};

let a, b

// "<b>abc</b>xyz<b>123</b>"
a = "abcxyz123"
b = ["abc","123"]
console.log(addBoldTag(a, b))

// "<b>aaabbc</b>c"
a = "aaabbcc"
b = ["aaa","aab","bc"]
console.log(addBoldTag(a, b))

// "aaabbcc"
a = "aaabbcc"
b = []
console.log(addBoldTag(a, b))

// "b<b>a</b>c<b>dc</b>b<b>cc</b>e<b>d</b>"
a = "bacdcbcced"
b = ["ccb","a","cc","dc","d"]
console.log(addBoldTag(a, b))

// "cb<b>ccceee</b>ad"
a = "cbccceeead"
b = ["e","cab","de","cc","db"]
console.log(addBoldTag(a, b))