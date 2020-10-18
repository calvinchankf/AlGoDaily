/*
    1st: iterative bfs
    
    Time    O(n)
    Space   O(h)
    92ms, faster than 33.86%
*/
var minDepth = function(root) {
    if (!root) {
        return 0
    }
    const q = [[root, 1]]
    let res = 10**4
    while (q.length > 0) {
        const [node, depth] = q.shift()
        
        if (node.left == null && node.right == null) {
            res = Math.min(res, depth)   
        }
        
        if (node.left) {
            q.push([node.left, depth + 1])
        }
        if (node.right) {
            q.push([node.right, depth + 1])
        }
    }
    return res
};

/*
    2nd: top-down recursive dfs

    Time    O(n)
    Space   O(h)
    280 ms, faster than 6.08%
*/
var minDepth = function(root) {
    
    if (!root) {
        return 0
    }
    
    let res = 10**4
    const dfs = (node, depth) => {
        if (!node) {
            return
        }
        if (node.left == null && node.right == null) {
            res = Math.min(res, depth)   
        }
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    }
    dfs(root, 1)
    
    return res
};

/*
    3rd: bottom-up recursive dfs

    Time    O(n)
    Space   O(h)
    260 ms, faster than 6.08%
*/
var minDepth = function(root) {
    if (!root) {
        return 0
    }
    let left = minDepth(root.left)
    let right = minDepth(root.right)
    if (root.right == null) {
        return left + 1
    }
    if (root.left == null) {
        return right + 1
    }
    return Math.min(left, right) + 1
};