/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st: recursive dfs

    Time    O(N)
    Space   O(N)
    96 ms, faster than 58.02%
*/
var getLonelyNodes = function(root) {
    
    const res = []
    
    const dfs = (node, peerCount) => {
        if (node == null) {
            return
        }
        if (peerCount == 1) {
            res.push(node.val)
        }
        let nextPeerCount = 0
        if (node.left) {
            nextPeerCount += 1
        }
        if (node.right) {
            nextPeerCount += 1
        }
        dfs(node.left, nextPeerCount)
        dfs(node.right, nextPeerCount)
    }
    dfs(root, 0)
    
    return res
};

/*
    3rd iterative breath first search

    Time    O(N)
    Space   O(N)
    96 ms, faster than 58.02%
*/
var getLonelyNodes = function(root) {
    const res = []
    const q = [[root, 0]]
    while (q.length > 0) {
        const [node, peerCount] = q.shift()
        if (peerCount == 1) {
            res.push(node.val)
        }
        let nextPeerCount = 0
        if (node.left) {
            nextPeerCount += 1
        }
        if (node.right) {
            nextPeerCount += 1
        }
        if (node.left) {
            q.push([node.left, nextPeerCount])
        }
        if (node.right) {
            q.push([node.right, nextPeerCount])
        }
    }
    return res
};