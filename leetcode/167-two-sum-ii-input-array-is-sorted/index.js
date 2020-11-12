/*
    2nd approach: 2 pointers

    Time	O(n)
    Space	O(1)
    68 ms, faster than 97.84%
*/
var twoSum = function(numbers, target) {
    let left = 0
    let right = numbers.length - 1
    while (left < right) {
        const total = numbers[left] + numbers[right]
        if (total < target) {
            left += 1
        } else if (total > target) {
            right -= 1
        } else {
            return [left+1, right+1]
        }
    }
    return [-1,-1]
};