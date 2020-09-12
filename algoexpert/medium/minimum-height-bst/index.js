function minHeightBst(array) {
	if (array.length == 0) {
		return null;
	}
	// Write your code here.
	const mid = Math.floor(array.length / 2);
	const node = new BST(array[mid]);
	node.left = minHeightBst(array.slice(0, mid));
	node.right = minHeightBst(array.slice(mid + 1));
	return node;
}

class BST {
	constructor(value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}

	insert(value) {
		if (value < this.value) {
			if (this.left === null) {
				this.left = new BST(value);
			} else {
				this.left.insert(value);
			}
		} else {
			if (this.right === null) {
				this.right = new BST(value);
			} else {
				this.right.insert(value);
			}
		}
	}
}

// Do not edit the line below.
exports.minHeightBst = minHeightBst;
