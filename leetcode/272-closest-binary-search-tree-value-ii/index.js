/*
    brute force

    Time    O(NlogN)
    Space   O(H)
    112 ms, faster than 17.50%
*/
var closestKValues = function (root, target, k) {
	let res = [];
	let cur = root;
	const inorder = (node) => {
		if (node == null) {
			return;
		}
		inorder(node.left);
		res.push(node.val);
		inorder(node.right);
	};
	inorder(root);
	res.sort((a, b) => {
		const x = Math.abs(a - target);
		const y = Math.abs(b - target);
		if (x < y) {
			return -1;
		}
		return 1;
	});
	return res.slice(0, k);
};
