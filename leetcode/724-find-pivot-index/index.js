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