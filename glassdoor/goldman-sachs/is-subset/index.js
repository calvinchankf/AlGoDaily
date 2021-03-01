/*
    https://www.1point3acres.com/bbs/thread-463866-1-1.html
*/
const isASubsetOfB = (A, B) => {
    const counter = {}
    for (let x of B) {
        if (x in counter === false) {
            counter[x] = 0
        }
        counter[x] += 1
    }
    for (let x of A) {
        if (x in counter === false) {
            return false
        }
        counter[x] -= 1
        if (counter[x] == 0) delete counter[x]
    }
    return true
}

let a, b

a = [4,5]
b = [2,4,5,6]
console.assert(isASubsetOfB(a, b) == true)

a = [4,5,5]
b = [2,4,5,6]
console.assert(isASubsetOfB(a, b) == false)

a = [4,5,5]
b = [2,4,5,5,6]
console.assert(isASubsetOfB(a, b) == true)

a = [4,5,5,5]
b = [2,4,5,5,6]
console.assert(isASubsetOfB(a, b) == false)

a = [4,7]
b = [2,4,5,6]
console.assert(isASubsetOfB(a, b) == false)