class Node {
	constructor() {
		this.children = {};
	}
}
class Trie {
	constructor() {
		this.root = new Node();
	}
	insert(word) {
		let cur = this.root;
		for (let c of word) {
			if (cur.children[c] === undefined) {
				cur.children[c] = new Node();
			}
			cur = cur.children[c];
		}
	}
	startsWith(prefix) {
		let cur = this.root;
		for (let c of prefix) {
			if (cur.children[c] === undefined) {
				return false;
			}
			cur = cur.children[c];
		}
		return true;
	}
}

function multiStringSearch(bigString, smallStrings) {
	// Write your code here.
	const words = bigString.split(" ");
	const trie = new Trie();
	for (let w of words) {
		for (let i = 0; i < w.length; i++) {
			const suffix = w.slice(i);
			trie.insert(suffix);
		}
	}

	const n = smallStrings.length;
	const res = Array(n).fill(false);
	for (let i = 0; i < n; i++) {
		const w = smallStrings[i];
		res[i] = trie.startsWith(w);
	}
	return res;
}

// Do not edit the line below.
exports.multiStringSearch = multiStringSearch;
