/*
    1st: hashtable

    Time    O(N)
    Space   O(N)
    128 ms, faster than 51.13%
*/
class SparseVector {
    constructor(nums) {
        this.cache = {}
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                this.cache[i] = nums[i]   
            }
        }
    }
    dotProduct(vec) {
        let res = 0
        for (let i in this.cache) {
            if (i in vec.cache) {
                res += this.cache[i] * vec.cache[i]
            }
        }
        return res
    }
}