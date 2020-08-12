function inOrderTraverse(tree, array) {
	// Write your code here.
	if (tree === null) {
		return;
	}
	inOrderTraverse(tree.left, array);
	array.push(tree.value);
	inOrderTraverse(tree.right, array);
	return array;
}

function preOrderTraverse(tree, array) {
	// Write your code here.
	if (tree === null) {
		return;
	}
	array.push(tree.value);
	preOrderTraverse(tree.left, array);
	preOrderTraverse(tree.right, array);
	return array;
}

function postOrderTraverse(tree, array) {
	// Write your code here.
	if (tree === null) {
		return;
	}
	postOrderTraverse(tree.left, array);
	postOrderTraverse(tree.right, array);
	array.push(tree.value);
	return array;
}

// Do not edit the lines below.
exports.inOrderTraverse = inOrderTraverse;
exports.preOrderTraverse = preOrderTraverse;
exports.postOrderTraverse = postOrderTraverse;
