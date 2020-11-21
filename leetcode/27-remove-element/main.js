/*
    1st: same logic as Quick Sort
    similar to lc283

    Time    O(N)
    Space   O(1)
    80 ms, faster than 61.45% 
*/
var removeElement = function(nums, val) {
    let j = 0
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] != val) {
            [nums[i], nums[j]] = [nums[j], nums[i]]
            j += 1
        }
    }
    return j
};

let a = [3, 2, 2, 3]
console.log(removeElement(a, 2))
console.log(a)

a = [0, 1, 2, 2, 3, 0, 4, 2]
console.log(removeElement(a, 2))
console.log(a)
