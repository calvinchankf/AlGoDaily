/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/*
    In short, just transform the tree into a graph and do bfs or dfs.

    e.g.
    {
        val1 : [parent1, left1, right1],
        val2 : [parent2, left2, right2],
        ....
    }

    Time    O(N)
    Space   O(N)
    84 ms, faster than 66.46%
*/
var distanceK = function (root, target, K) {
	const connections = {};
	const buildGraph = (node, parent) => {
		if (node === null) {
			return;
		}
		const neighbours = [parent, -1, -1];
		if (node.left) {
			neighbours[1] = node.left.val;
		}
		if (node.right) {
			neighbours[2] = node.right.val;
		}
		connections[node.val] = neighbours;
		buildGraph(node.left, node.val);
		buildGraph(node.right, node.val);
	};
	buildGraph(root, -1);
	const res = [];
	const seen = {};
	const q = [[target.val, 0]];
	while (q.length > 0) {
		const [node, steps] = q.pop(0);
		if (node == -1) {
			continue;
		}
		if (node in seen) {
			continue;
		}
		seen[node] = true;
		if (steps == K) {
			res.push(node);
		}
		const neighbours = connections[node];
		for (let nb of neighbours) {
			q.push([nb, steps + 1]);
		}
	}
	return res;
};
