/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @param {number[]} arr3
 * @return {number[]}
 */
var arraysIntersection = function(arr1, arr2, arr3) {
    const ht = {}
    for (let x of arr1) {
        if (ht[x] === undefined) {
            ht[x] = 0
        }
        ht[x] += 1
    }
    for (let x of arr2) {
        if (ht[x] === undefined) {
            ht[x] = 0
        }
        ht[x] += 1
    }
    for (let x of arr3) {
        if (ht[x] === undefined) {
            ht[x] = 0
        }
        ht[x] += 1
    }
    const res = []
    for (let key in ht) {
        if (ht[key] === 3) {
            res.push(key)
        }
    }
    return res
};