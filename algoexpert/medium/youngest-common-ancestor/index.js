/*
    Good question: here we dont use children but ancestor for each node
    - bottom up to find out path
    - the common suffix is the result
*/

// This is an input class. Do not edit.
class AncestralTree {
	constructor(name) {
		this.name = name;
		this.ancestor = null;
	}
}

function getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo) {
	// Write your code here.
	const path1 = []; // I, D, B, A
	let cur = descendantOne;
	while (cur !== null) {
		path1.push(cur);
		cur = cur.ancestor;
	}

	const path2 = []; // E, B, A
	cur = descendantTwo;
	while (cur !== null) {
		path2.push(cur);
		cur = cur.ancestor;
	}

	let res = null;
	while (path1.length > 0 && path2.length > 0) {
		const a = path1.pop();
		const b = path2.pop();
		if (a != b) {
			break;
		}
		res = a;
	}

	return res;
}

// Do not edit the lines below.
exports.AncestralTree = AncestralTree;
exports.getYoungestCommonAncestor = getYoungestCommonAncestor;
