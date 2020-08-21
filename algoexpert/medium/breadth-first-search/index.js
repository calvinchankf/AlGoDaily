// Do not edit the class below except
// for the breadthFirstSearch method.
// Feel free to add new properties
// and methods to the class.
class Node {
	constructor(name) {
		this.name = name;
		this.children = [];
	}

	addChild(name) {
		this.children.push(new Node(name));
		return this;
	}

	breadthFirstSearch(array) {
		// Write your code here.
		array.push(this.name);

		const q = [];
		for (let child of this.children) {
			q.push(child);
		}

		while (q.length > 0) {
			const node = q.shift();
			array.push(node.name);
			for (let child of node.children) {
				q.push(child);
			}
		}
		return array;
	}
}

// Do not edit the line below.
exports.Node = Node;
