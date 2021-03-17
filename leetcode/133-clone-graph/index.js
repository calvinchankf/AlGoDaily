/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/*
    1st: DFS
    - use the return of each recursion

    Time    O(N)
    Space   O(N)
    76 ms, faster than 86.98%
*/
var cloneGraph = function(node) {
    return build(node, {})
};

const build = (node, cache) => {
    if (node == null) {
        return null
    }
    if (node.val in cache) {
        return cache[node.val]
    }
    const clone = new Node(node.val)
    cache[node.val] = clone
    for (let nb of node.neighbors) {
        const temp = build(nb, cache)
        if (temp != null) {
            clone.neighbors.push(temp)   
        }
    }
    return clone
}