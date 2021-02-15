/*
    1st approach: recursion
	- if a node is within the range, return it and REMEMBER to reset its left and right if necessary

	Time		O(N)
	Space		O(N)
    160 ms, faster than 6.07%
*/
var trimBST = function(root, low, high) {
    return trim(root, low, high)
};

const trim = (node, low, high) => {
    if (node == null) {
        return null
    }
    // console.log('low, high', node.val, low)
    if (node.val < low) {
        return trim(node.right, low, high)
    }
    if (node.val > high) {
        return trim(node.left, low, high)
    }
    node.left = trim(node.left, low, high)
    node.right = trim(node.right, low, high)
    return node
}