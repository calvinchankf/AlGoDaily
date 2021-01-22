/*
    Given a string S and a list of words A, find out the longest word(s) from A which can be formed using the characters from S

    e.g.1
    Input:
    toe, [to, toe, toes]
    Output:
    [toe]

    e.g.2
    Input:
    toe, [to, toe, toes, eot]
    Output:
    [toe, eot]

    e.g.3
    Input:
    toe, [to, toe, toes, eott]
    Output:
    [toe]

    ref:
    - my interview
*/
const longestWordMade = (S, A) => {
    const targetCounter = buildHt(S)
    let res = []
    let maxLen = 0
    for (let w of A) {
        const counter = buildHt(w)
        let didContain = true
        for (let c in counter) {
            if (c in targetCounter == false || counter[c] > targetCounter[c]) {
                didContain = false
                break
            }
        }
        if (didContain == false) continue

        if (w.length > maxLen) {
            maxLen = w.length
            res = [w]
        } else if (w.length == maxLen) {
            res.push(w)
        }
    }
    return res
}

const buildHt = (S) => {
    const counter = {}
    for (let c of S) {
        if (c in counter == false) {
            counter[c] = 0
        }
        counter[c] += 1
    }
    return counter
}

let a, b

a = 'toe'
b = ['to', 'toe', 'toes']
console.log(longestWordMade(a, b))

a = 'toe'
b = ['to', 'toe', 'toes', 'eot']
console.log(longestWordMade(a, b))

a = 'toe'
b = ['to', 'toe', 'toes', 'eott']
console.log(longestWordMade(a, b))

a = 'ttoe'
b = ['to', 'toe', 'toes', 'eott']
console.log(longestWordMade(a, b))

a = 'ttoe'
b = ['to', 'ttoe', 'toes', 'eott']
console.log(longestWordMade(a, b))