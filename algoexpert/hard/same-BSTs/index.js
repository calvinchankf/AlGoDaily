/*
    1st: construct BST
*/
class Node {
	constructor(val) {
		this.val = val;
		this.left = null;
		this.right = null;
	}
}

const insertBST = (root, x) => {
	let cur = root;
	while (cur != null) {
		if (x < cur.val) {
			if (cur.left === null) {
				cur.left = new Node(x);
				return;
			} else {
				cur = cur.left;
			}
		} else if (x >= cur.val) {
			if (cur.right === null) {
				cur.right = new Node(x);
				return;
			} else {
				cur = cur.right;
			}
		}
	}
};

const isSameBST = (node1, node2) => {
	if (node1 == null && node2 == null) {
		return true;
	} else if (node1 == null || node2 == null) {
		return false;
	}
	if (node1.val != node2.val) {
		return false;
	}
	return (
		isSameBST(node1.left, node2.left) && isSameBST(node1.right, node2.right)
	);
};

function sameBsts(arrayOne, arrayTwo) {
	// Write your code here.
	let root1 = new Node(arrayOne[0]);
	for (let i = 1; i < arrayOne.length; i++) {
		insertBST(root1, arrayOne[i]);
	}
	let root2 = new Node(arrayTwo[0]);
	for (let i = 1; i < arrayTwo.length; i++) {
		insertBST(root2, arrayTwo[i]);
	}
	return isSameBST(root1, root2);
}

// Do not edit the line below.
exports.sameBsts = sameBsts;
