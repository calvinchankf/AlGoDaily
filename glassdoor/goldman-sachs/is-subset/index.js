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
        if (x in counter === false || counter[x] === 0) {
            return false
        }
        counter[x] -= 1
    }
    return true
}

let a, b

a = [4,5]
b = [2,4,5,6]
console.log(isASubsetOfB(a, b))

a = [4,5,5]
b = [2,4,5,6]
console.log(isASubsetOfB(a, b))

a = [4,5,5]
b = [2,4,5,5,6]
console.log(isASubsetOfB(a, b))

a = [4,5,5,5]
b = [2,4,5,5,6]
console.log(isASubsetOfB(a, b))

a = [4,7]
b = [2,4,5,6]
console.log(isASubsetOfB(a, b))