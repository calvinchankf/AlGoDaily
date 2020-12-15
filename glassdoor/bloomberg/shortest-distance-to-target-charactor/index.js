/*
    lets say u r give a string and a character, find the shortest index distance from every character to the target character

    e.g.
    s = 'bloomberg', target = 'b'

    result = [0, 1, 2, 2, 1, 0, 1, 2, 3]

    Explanation:
    
    b l o o m b e r g
    0 1 2 2 1 0 1 2 3
      < < > >   < < <

    Assume the input only allows lowercase letters
*/

/*
    Approach

        b l o o m b e r g
    ->  0 1 2 3 4 0 1 2 3
    <-  0 4 3 2 1 0 * * *
        -----------------
        0 1 2 2 1 0 1 2 3 <- result
*/
const shortestDistances = (s, target) => {
    const n = s.length
    const forward = Array(n).fill(2**32)
    const backward = Array(n).fill(2**32)
    let targetIdx = -1 
    for (let i = 0; i < n; i++) {
        if (s[i] == target) {
            targetIdx = i
        }
        if (targetIdx != -1) {
            forward[i] = i - targetIdx
        }
    }
    targetIdx = -1 
    for (let i = n-1; i >= 0; i--) {
        if (s[i] == target) {
            targetIdx = i
        }
        if (targetIdx != -1) {
            backward[i] = targetIdx - i
        }
    }
    const res = Array(n).fill(2**32)
    for (let i = 0; i < n; i++) {
        res[i] = Math.min(forward[i], backward[i])
        if (res[i] == 2**32) {
            res[i] = -1
        }
    }
    return res
}

let a, b

a = 'bloomberg'
b = 'b'
console.log(shortestDistances(a, b))

a = 'bloomberg'
b = 'z'
console.log(shortestDistances(a, b))