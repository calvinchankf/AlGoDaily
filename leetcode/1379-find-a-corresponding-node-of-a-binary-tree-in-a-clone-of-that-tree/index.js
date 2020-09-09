/*
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
