/*
    1st: BFS
    
    Time    O(N)
    Space   O(H)
    96 ms, faster than 10.11% 
*/
var zigzagLevelOrder = function (root) {
	if (root === null || root === undefined) {
		return [];
	}
	var result = [];
	var queue = [];
	queue.push(root);
	while (queue.length > 0) {
		var level = [];
		var lengthOnLevel = queue.length;
		for (let i = 0; i < lengthOnLevel; i++) {
			var deq = queue.shift();
			level.push(deq.val);
			if (deq.left !== null) {
				queue.push(deq.left);
			}
			if (deq.right !== null) {
				queue.push(deq.right);
			}
		}
		if (result.length % 2 === 0) {
			result.push(level);
		} else {
			result.push(level.reverse());
		}
	}
	return result;
};
