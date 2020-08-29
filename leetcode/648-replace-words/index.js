/*
    1st: trie
    
    Time    O(N)
    Space   O(N)
    108 ms, faster than 91.26%
*/
class Node {
	constructor() {
		this.children = {};
		this.isWord = false;
	}
}

class Trie {
	constructor() {
		this.root = new Node();
	}
	insert(key) {
		let cur = this.root;
		for (let c of key) {
			if (cur.children[c] === undefined) {
				cur.children[c] = new Node();
			}
			cur = cur.children[c];
		}
		cur.isWord = true;
	}
	search(key) {
		let cur = this.root;
		let res = "";
		for (let c of key) {
			if (cur.isWord) {
				return res;
			}
			if (cur.children[c] === undefined) {
				return null;
			}
			cur = cur.children[c];
			res += c;
		}
	}
}

var replaceWords = function (dictionary, sentence) {
	const trie = new Trie();
	for (let w of dictionary) {
		trie.insert(w);
	}
	let words = sentence.split(" ");
	let res = "";
	for (let w of words) {
		const temp = trie.search(w);
		if (temp == null) {
			res += w + " ";
		} else {
			res += temp + " ";
		}
	}
	return res.trim();
};
