/*
    1st approach: bfs
    - declare a result array
    - when we traverse down, put the val into the result if the depth >= len(array)

    Time    O(n)
    Space   O(h)
    104 ms, faster than 17.31%
*/
var rightSideView = function (root) {
	if (!root) {
		return [];
	}
	const res = [];
	const q = [[root, 0]];
	while (q.length > 0) {
		const [node, depth] = q.shift();

        // we can also do it with a hashtable
		if (depth >= res.length) {
			res.push(node.val);
		}

		if (node.right) {
			q.push([node.right, depth + 1]);
		}
		if (node.left) {
			q.push([node.left, depth + 1]);
		}
	}
	return res;
};

/*
    2nd approach: dfs
    - declare a result array
    - when we traverse down, put the val into the result if the depth >= len(array)

    Time    O(n)
    Space   O(h)
    80 ms, faster than 81.25%
*/
var rightSideView = function(root) {
    if (root === null) {
        return []
    }
    const res = []
    
    const dfs = (node, level) => {
        if (node === null) {
            return
        }
        if (level >= res.length) {
            res.push(node.val)
        }
        dfs(node.right, level + 1)
        dfs(node.left, level + 1)
    }
    dfs(root, 0)
    
    return res
};