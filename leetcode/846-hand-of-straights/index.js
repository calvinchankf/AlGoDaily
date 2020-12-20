/*
    1st: sort + hashtable
    - put every number counter
    - sort the array
    - for each unused number, try to see if we can form a sequence(in length of K)

    Time    O(NlogN + NK)
    Space   O(N)
    132 ms, faster than 59.20%
*/
var isNStraightHand = function(nums, k) {
    const n = nums.length
    const counter = {}
    for (let x of nums) {
        if (x in counter == false) {
            counter[x] = 0
        }
        counter[x] += 1
    }
    nums.sort((a, b) => a - b)
    for (let i = 0; i < n; i++) {
        const x = nums[i]
        if (x in counter === false) {
            continue
        }
        const seq = [x]
        let cur = x
        counter[cur] -= 1
        if (counter[cur] == 0) delete counter[cur]
        while (seq[seq.length-1] + 1 in counter && seq.length < k) {
            cur += 1
            seq.push(cur)
            counter[cur] -= 1
            if (counter[cur] == 0) delete counter[cur]
        }
        if (seq.length != k) {
            return false
        }
    }
    return true
};