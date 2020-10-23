/*
    https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=663239&ctid=230547

    Given an array of objects, start and end as indices, reverse the the array of objects from start to end
*/
const reverseSubarray = (arr, start, end) => {
    if (Array.isArray(arr) === false || start >= end || start < 0 || end >= arr.length) {
        return
    }
    let i = start
    let j = end
    while (i < j) {
        const temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    }
}

const a = [0,1,2,3,4,5,6,7,8,9]
let b

b = [...a]
reverseSubarray(b, 0, 9)
console.log(b)

b = [...a]
reverseSubarray(b, 1, 8)
console.log(b)

b = [...a]
reverseSubarray(b, 4, 5)
console.log(b)

b = [...a]
reverseSubarray(b, 5, 5)
console.log(b)

b = [...a]
reverseSubarray(b, 5, 4)
console.log(b)