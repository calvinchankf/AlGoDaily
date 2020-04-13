/**
 *  Attempt 2: math
    2(a+b+c)-(2a+2b+c) = c
    O(n+n) with O(n) space
    beats 51.63%
 */
var singleNumber = function(nums) {
    const hs = new Set()
    nums.forEach(num => {
        if (hs.has(num)) {
            hs.delete(num)
        } else {
            hs.add(num)
        }
    })
    for (const key of hs) {
        return key
    }
};

/**
 *  Attempt 3: beat operation
    use XOR: exclusive or
    A	B		XOR(^)
    F	F		F
    F	T		T
    T	F		T
    T	T		F
    beats 100%
 */

var singleNumber = function(nums) {
    let res = 0
    nums.forEach(num => {
        res = res^num  
    })
    return res
};