/*
    2nd: similar logic as min stack
    - similar to lc155

    e.g.
    stack = [1,2,3,4,5], maxSize = 5

    increment(2, 100) => stack = [1, 2,   3, 4, 5]
                        incres = [0, 0, 100, 0, 5]
    increment(9, 100) => stack = [1, 2,   3, 4,   5]
                        incres = [0, 0, 100, 0, 105]

    when we pop(), we add the increment to the stack[-1]
    pop() returns 5 + 100 = 105
    the stack becomes    stack = [1, 2,   3,   4]
                        incres = [0, 0, 100, 100]

    when we pop() again, do the same thing
    pop() returns 4 + 100 = 104
    the stack becomes    stack = [1, 2,   3]
                        incres = [0, 0, 200]
    
    when we pop() again, do the same thing
    pop() returns 3 + 200 = 203
    the stack becomes    stack = [1,   2]
                        incres = [0, 200]

    ref:
    https://leetcode.com/problems/design-a-stack-with-increment-operation/discuss/542205/Python-Prefix-sum-with-1-array

    Time    O(1)
    Space   O(1)
    132 ms, faster than 59.04%
*/


/**
 * @param {number} maxSize
 */
var CustomStack = function(maxSize) {
    this.maxSize = maxSize
    this.stack = []
};

/** 
 * @param {number} x
 * @return {void}
 */
CustomStack.prototype.push = function(x) {
    if (this.stack.length < this.maxSize) {
        this.stack.push([x, 0])
    }
};

/**
 * @return {number}
 */
CustomStack.prototype.pop = function() {
    if (this.stack.length == 0) {
        return -1
    }
    let [res, inc] = this.stack.pop()
    res += inc
    
    if (this.stack.length > 0) {
        this.stack[this.stack.length-1][1] += inc
    }
    return res
};

/** 
 * @param {number} k 
 * @param {number} val
 * @return {void}
 */
CustomStack.prototype.increment = function(k, val) {
    if (this.stack.length > 0) {
        k = Math.min(k, this.stack.length)
        this.stack[k-1][1] += val
    }
};

/** 
 * Your CustomStack object will be instantiated and called as such:
 * var obj = new CustomStack(maxSize)
 * obj.push(x)
 * var param_2 = obj.pop()
 * obj.increment(k,val)
 */