/*
    1st: 2 arrays
    
    Time    O(3N)
    Space   O(2N)
    172 ms, faster than 56.15% 
*/
var pivotIndex = function(nums) {
    const n = nums.length
    let pfs = 0
    const pfss = Array(n).fill(0)
    for (let i = 0; i < n; i++) {
        pfs += nums[i]
        pfss[i] = pfs
    }
    let sfs = 0
    const sfss = Array(n).fill(0)
    for (let i = n-1; i >= 0; i--) {
        sfs += nums[i]
        sfss[i] = sfs
    }
    for (let i = 0; i < n; i++) {
        if (pfss[i] == sfss[i]) { return i }
    }
    return -1
};

/*
    2nd: 
    - similar to lc238, 724
    - at every index subtract prefix sum from the right until prefix sum == suffix sum

    [1, 7, 3, 6, 5, 6]
     1  8 11 17 22 28
             17 11 6
             ^
    
    Time    O(2N)
    Space   O(1)
    108 ms, faster than 98.64%
*/
var pivotIndex = function(nums) {
    const n = nums.length
    let pfs = 0
    nums.forEach(x => pfs += x)
    let sfs = 0
    let res = -1
    for (let i = n - 1; i >=0; i--) {
        sfs += nums[i]
        if (sfs == pfs) {
            res = i
        }
        pfs -= nums[i]
    }
    return res
};