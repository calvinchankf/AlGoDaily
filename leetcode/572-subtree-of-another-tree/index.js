/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/*
    1st approach: brute force checking
    - for each node, check it equals to target tree

    Time    O(S^2)
    Space   O(H)
    112 ms, faster than 45.39% 
*/
var isSubtree = function (s, t) {
	return f(s, t);
};

const f = (a, b) => {
	if (a == null && b == null) {
		return true;
	}
	if (a == null || b == null) {
		return false;
	}
	if (a.val == b.val) {
		const bool = check(a, b);
		if (bool) {
			return true;
		}
	}
	return f(a.left, b) || f(a.right, b);
};

const check = (a, b) => {
	if (a == null && b == null) {
		return true;
	}
	if (a == null || b == null) {
		return false;
	}
	if (a.val == b.val) {
		const left = check(a.left, b.left);
		const right = check(a.right, b.right);
		return left && right;
	}
	return false;
};

/*
    2nd approach:
    - serialize both trees
    - check if the 2nd serialized representation is within the 1st serialized representation

    e.g
                3
            4       5
        1     2
    0
    serialized = (3(4(1(0()())())(2()()))(5()()))

    corner case: [12] and [2]
    - so we have to wrap the whole tree within a pair of parentheses

    Time    O(S+T)
    Space   O(h)
    96 ms, faster than 86.02%
*/
var isSubtree = function (s, t) {
	if (s == null && t == null) {
		return true;
	}
	if (s == null || t == null) {
		return false;
	}
	const a = serialize(s);
	const b = serialize(t);
	return a.includes(b);
};

const serialize = (node) => {
	if (node == null) {
		return "()";
	}
	const left = serialize(node.left);
	const right = serialize(node.right);
	return `(${node.val}${left}${right})`;
};
