// Do not edit the class below except
// for the depthFirstSearch method.
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

	depthFirstSearch(array) {
		// Write your code here.
		const dfs = (node) => {
			if (node === undefined) {
				return;
			}
			array.push(node.name);
			for (let child of node.children) {
				dfs(child);
			}
		};
		array.push(this.name);
		for (let child of this.children) {
			dfs(child);
		}
		return array;
	}
}

// Do not edit the line below.
exports.Node = Node;
