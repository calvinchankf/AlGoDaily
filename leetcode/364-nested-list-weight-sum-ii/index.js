/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * function NestedInteger() {
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     @return {boolean}
 *     this.isInteger = function() {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     @return {integer}
 *     this.getInteger = function() {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a single integer equal to value.
 *     @return {void}
 *     this.setInteger = function(value) {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 *     @return {void}
 *     this.add = function(elem) {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds, if it holds a nested list
 *     Return null if this NestedInteger holds a single integer
 *     @return {NestedInteger[]}
 *     this.getList = function() {
 *         ...
 *     };
 * };
 */

/*
    2nd approach: recursion + hashtable
    - recursively put the items into the appropriate array at index(key in hashtable)
    - find out the max depth that we can reach
    - multiply the values with index and sum them up to the result

    Time    O(2n)
    Space   O(h)
    76 ms, faster than 80.00% 
*/
var depthSumInverse = function(nestedList) {
    
    const ht = {}
    let maxDepth = 0
    
    const dfs = (arr, depth) => {
        // update maxDepth
        maxDepth = Math.max(maxDepth, depth)
        // init ht[depth] if not existed
        if (depth in ht === false) {
            ht[depth] = []
        }
        // recursion
        for (let x of arr) {
            if (x.isInteger()) {
                ht[depth].push(x.getInteger())
            } else {
                dfs(x.getList(), depth + 1)
            }
        }
    }
    dfs(nestedList, 1)
    // calculation
    let res = 0
    for (let depth in ht) {
        const d = maxDepth - depth + 1
        for (let num of ht[depth]) {
            res += d * num
        }
    }
    return res
};