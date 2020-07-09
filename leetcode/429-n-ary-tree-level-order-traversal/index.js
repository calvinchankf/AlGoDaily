/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */
/**
 * @param {Node} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
	if (root === null || root === undefined) {
		return [];
	}
	var result = [];
	var queue = [];
	queue.push(root);
	while (queue.length > 0) {
		var level = [];
		var count = queue.length;
		for (let i = 0; i < count; i++) {
			var node = queue.shift();
			level.push(node.val);
			for (let child of node.children) {
				queue.push(child);
			}
		}
		result.push(level);
	}
	return result;
};
