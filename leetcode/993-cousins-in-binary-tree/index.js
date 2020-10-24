/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/*
    1st approach: BFS
    - BFS the tree level by level
    - after we have done the iterating one level, check if the x, y are on the same level and have diff parents

    Time    O(n)
    Space   O(n)
    12ms beats 100%
*/
var isCousins = function (root, x, y) {
	let xParent = null;
	let xDepth = -1;
	let yParent = null;
	let yDepth = -1;

	let q = [[root, null, 0]];
	while (q.length > 0) {
		const [node, parent, depth] = q.pop(0);
		if (node.val == x) {
			xParent = parent;
			xDepth = depth;
		}
		if (node.val == y) {
			yParent = parent;
			yDepth = depth;
		}
		if (node.left) {
			q.push([node.left, node, depth + 1]);
		}
		if (node.right) {
			q.push([node.right, node, depth + 1]);
		}
	}
	return xDepth == yDepth && xParent != yParent;
};

/*
    2nd approach: BFS
    - BFS the tree level by level
    - after we have done the iterating one level, check if the x, y are on the same level and have diff parents

    Time    O(n)
    Space   O(n)
    88 ms, faster than 35.80%
*/
var isCousins = function(root, x, y) {
    if (!root || x == y) {
        return false
    }
    const q = [[root, null]]
    while (q.length > 0) {
        const n = q.length
        
        let foundNode = null
        let foundNodeParent = null
        
        for (let i = 0; i < n; i++) {
            const [node, parent] = q.shift()
            if (node.val == x || node.val == y) {
                if (foundNode && foundNodeParent != parent) {
                    return true
                }
                foundNode = node
                foundNodeParent = parent
            }
            if (node.left) {
                q.push([node.left, node])
            }
            if (node.right) {
                q.push([node.right, node])
            }
        }
    }
    return false
};

/*
    3rd approach: recursive dfs
    - DFS the tree 
    - after we have done the iterating one level, check if the x, y are on the same level and have diff parents

    Time    O(n)
    Space   O(n)
    88 ms, faster than 35.80%
*/
var isCousins = function(root, x, y) {
    if (!root || x == y) {
        return false
    }
    const [xDepth, xParent] = findDepth(root, null, x)
    const [yDepth, yParent] = findDepth(root, null, y)
    return xDepth == yDepth && xParent != yParent
};

const findDepth = (node, parent, target) => {
    if (node == null) {
        return [-1, null]
    }
    if (node.val == target) {
        return [0, parent]
    }
    const left = findDepth(node.left, node, target)
    const right = findDepth(node.right, node, target)
    if (left[0] != -1) {
        return [left[0] + 1, left[1]]
    }
    if (right[0] != -1) {
        return [right[0] + 1, right[1]]
    }
    return [-1, null]
}