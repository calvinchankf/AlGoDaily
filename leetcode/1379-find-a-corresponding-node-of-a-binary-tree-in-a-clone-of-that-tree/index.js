/*
    1st: recursive DFS

    Time    O(N)
    Space   O(H)
    316 ms, faster than 76.83%
*/
var getTargetCopy = function (original, cloned, target) {
	if (original == null || cloned == null) {
		return null;
	}
	if (original == target) {
		return cloned;
	}
	let left = getTargetCopy(original.left, cloned.left, target);
	if (left !== null) {
		return left;
	}
	let right = getTargetCopy(original.right, cloned.right, target);
	if (right !== null) {
		return right;
	}
	return null;
};

/*
    2nd: BFS

    Time    O(N)
    Space   O(H)
    304 ms, faster than 93.42%
*/
var getTargetCopy = function(original, cloned, target) {
    const q = [[original, cloned]]
    while (q.length > 0) {
        const [a, b] = q.shift()
        if (a === target) {
            return b
        }
        if (a.left && b.left) {
            q.push([a.left, b.left])
        }
        if (a.right && b.right) {
            q.push([a.right, b.right])
        }
    }
    return null
};