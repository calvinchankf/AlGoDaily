/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/*
    1st approach: bfs

    Time    O(n)
    Space   O(2w)
    100 ms, faster than 67.75%
*/
var connect = function(root) {
    if (!root) {
        return null
    }
    const q = [root]
    while (q.length > 0) {
        let prev = null
        const n = q.length
        for (let i = 0; i < n; i++) {
            const node= q.shift()
            node.next = prev
            prev = node
            if (node.right) {
                q.push(node.right)
            }
            if (node.left) {
                q.push(node.left)
            }
        }
    }
    return root
};