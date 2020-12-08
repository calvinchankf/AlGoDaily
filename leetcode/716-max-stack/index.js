/*
    Easier approach: sorted list + stack

    Time of
    - push()      O(logN + K)
    - pop()       O(logN + K)
    - top()       O(1)
    - peekMax()   O(1)
    - popMax()    O(K)
    152 ms, faster than 95.57%
*/
class MaxStack {
    constructor() {
        this.sortedNums = []
        this.stack = []
    }
    push(x) {
        this.stack.push(x)
        const i = this._upperBsearch(this.sortedNums, x)
        this.sortedNums.splice(i, 0, x)
    }
    pop() {
        const res = this.stack.pop()
        const i = this._upperBsearch(this.sortedNums, res)
        this.sortedNums.splice(i-1, 1)
        return res
    }
    top() {
        const n = this.stack.length
        return this.stack[n-1]
    }
    peekMax() {
        const n = this.sortedNums.length
        return this.sortedNums[n-1]
    }
    popMax() {
        const res = this.sortedNums.pop()
        const n = this.stack.length
        for (let i = n-1; i >= 0; i--) {
            if (this.stack[i] == res) {
                this.stack.splice(i, 1)
                break
            }
        }
        return res
    }
    _upperBsearch(nums, target) {
        let left = 0;
        let right = nums.length;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (target >= nums[mid]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}