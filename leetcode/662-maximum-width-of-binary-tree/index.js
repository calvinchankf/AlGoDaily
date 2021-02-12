/*
    1st approach: bfs + math
    - calculate the position of a node in the full binary tree
        left = position*2 + 0
        right = position*2 + 1
    - bfs the btree level by level to get the leftmost and the rightmost nodes' position as if they are in a full binary tree
        diff = right pos - left pos + 1
    - if diff > res, override the result

    *** caution ***
    - to prevent overflow, reset the leftmost idx to 0 when we go down the tree

    Time    O(n)
    Space   O(h)
    80 ms, faster than 99.24%
*/
var widthOfBinaryTree = function (root) {
	let res = 0;
	const q = [[root, 0]];
	while (q.length > 0) {
		const n = q.length;
		let left = 0;
		let right = 0;
		for (let i = 0; i < n; i++) {
			const [node, idx] = q.shift();
			if (i == 0) {
				left = idx;
			}
			if (i + 1 == n) {
				right = idx;
			}
			if (node.left) {
				q.push([node.left, (idx - left) * 2]);
			}
			if (node.right) {
				q.push([node.right, (idx - left) * 2 + 1]);
			}
		}
		res = Math.max(res, right - left + 1);
	}
	return res;
};
